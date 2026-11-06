#!/usr/bin/env python3
"""
IFC -> PostGIS-tabel met drie detailniveaus (LOD's), als invoer voor pg2b3dm.

  lod 0  blok: de footprint van het hele gebouw, van laagste tot hoogste punt (LOD1)
  lod 1  per verdieping een blok met de footprint van die verdieping
  lod 2  alle elementen uit de IFC (volledig detail)

De IFC moet gegeorefereerd zijn (IfcMapConversion naar EPSG:28992, RD).
Hoogtes in de IFC worden gelezen als NAP en omgerekend naar hoogte boven de
ellipsoide (EPSG:4979), zodat het gebouw in Cesium op het terrein staat.

Gebruik (in de ifc-container):
  ifc_naar_lod.py architectuur.ifc --model Architectuur
  ifc_naar_lod.py constructie.ifc --model Constructie --toevoegen --alleen-detail
  ifc_naar_lod.py installaties.ifc --model Installaties --alleen IfcPipeSegment --toevoegen --alleen-detail
"""
import argparse
import multiprocessing
import sys
import time

import numpy as np
import psycopg
import shapely
from shapely.geometry import MultiPoint, Polygon
from shapely.ops import unary_union

import ifcopenshell
import ifcopenshell.geom
import ifcopenshell.util.element as ue
import ifcopenshell.util.unit as uu

# Alle fysieke elementen (IfcElement: bouwdelen, installaties, meubilair).
# Sparingen (IfcFeatureElement) en virtuele elementen laten we weg.
WEGLATEN = ["IfcFeatureElement", "IfcVirtualElement"]


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def map_conversion(f):
    """Lees de georeferentie (IfcMapConversion) uit de IFC."""
    mcs = f.by_type("IfcMapConversion")
    if not mcs:
        sys.exit("Geen IfcMapConversion gevonden: de IFC is niet gegeorefereerd.")
    mc = mcs[0]
    crs = mc.TargetCRS.Name if mc.TargetCRS else "?"
    if "28992" not in crs:
        log(f"Let op: doel-CRS is {crs}, dit script gaat uit van EPSG:28992 (RD).")
    a = mc.XAxisAbscissa if mc.XAxisAbscissa is not None else 1.0
    o = mc.XAxisOrdinate if mc.XAxisOrdinate is not None else 0.0
    n = (a * a + o * o) ** 0.5
    # IfcOpenShell levert coordinaten in meters. Scale vertaalt projecteenheden
    # naar kaarteenheden; omgerekend naar meters is de factor Scale / eenheid.
    unit = uu.calculate_unit_scale(f)
    s = (mc.Scale / unit) if mc.Scale is not None else 1.0
    return dict(e=mc.Eastings, n=mc.Northings, h=mc.OrthogonalHeight or 0.0,
                cos=a / n, sin=o / n, s=s, crs=crs)


def naar_rd(v, m):
    """Lokale IFC-coordinaten (meters) -> RD x, y en NAP-hoogte."""
    x, y, z = v[:, 0], v[:, 1], v[:, 2]
    return np.column_stack([
        m["e"] + m["s"] * (x * m["cos"] - y * m["sin"]),
        m["n"] + m["s"] * (x * m["sin"] + y * m["cos"]),
        m["h"] + m["s"] * z,
    ])


def verdieping(el):
    """De verdieping (IfcBuildingStorey) waar een element in staat."""
    while el is not None:
        c = ue.get_container(el)
        if c is not None:
            return c if c.is_a("IfcBuildingStorey") else None
        el = ue.get_aggregate(el)
    return None


def tin_wkt(tris):
    """Driehoeken (m x 3 x 3) -> EWKT van een TIN Z in RD + NAP (EPSG:7415)."""
    parts = []
    for t in tris:
        p = ",".join(f"{x:.3f} {y:.3f} {z:.3f}" for x, y, z in (t[0], t[1], t[2], t[0]))
        parts.append(f"(({p}))")
    return "SRID=7415;TIN Z (" + ",".join(parts) + ")"


def extrudeer(poly, z0, z1):
    """Polygoon -> gesloten blok van driehoeken tussen hoogte z0 en z1."""
    tris = []
    for t in shapely.constrained_delaunay_triangles(poly).geoms:
        c = list(t.exterior.coords)[:3]
        tris.append([(x, y, z1) for x, y in c])            # dak
        tris.append([(x, y, z0) for x, y in reversed(c)])  # bodem
    for ring in [poly.exterior, *poly.interiors]:
        cs = list(ring.coords)
        for (x1, y1), (x2, y2) in zip(cs[:-1], cs[1:]):    # gevels
            tris.append([(x1, y1, z0), (x2, y2, z0), (x2, y2, z1)])
            tris.append([(x1, y1, z0), (x2, y2, z1), (x1, y1, z1)])
    return np.array(tris)


def footprint(hulls):
    """Voeg de 2D-omtrekken van elementen samen tot een nette footprint."""
    fp = unary_union(hulls)
    fp = fp.buffer(0.5, join_style="mitre").buffer(-0.5, join_style="mitre").simplify(0.2)
    polys = [fp] if isinstance(fp, Polygon) else list(getattr(fp, "geoms", []))
    return [p for p in polys if p.area > 25.0]   # snippers weglaten


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ifc", help="IFC-bestand")
    ap.add_argument("--tabel", default="public.parkeergarage_lod", help="doeltabel in PostGIS")
    ap.add_argument("--model", default="Architectuur",
                    help="naam van het model, komt in de kolom 'model' (standaard: Architectuur)")
    ap.add_argument("--zonder", nargs="*", default=[], metavar="KLASSE",
                    help="IFC-klassen die je niet wilt meenemen, bijv. --zonder IfcMember IfcRailing")
    ap.add_argument("--alleen", nargs="*", default=[], metavar="KLASSE",
                    help="neem alleen deze IFC-klassen mee, bijv. --alleen IfcPipeSegment")
    ap.add_argument("--toevoegen", action="store_true",
                    help="voeg toe aan een bestaande tabel in plaats van die opnieuw te maken")
    ap.add_argument("--alleen-detail", action="store_true",
                    help="alleen lod 2 (de elementen), geen blokken voor lod 0 en lod 1")
    args = ap.parse_args()

    settings = ifcopenshell.geom.settings()
    settings.set("use-world-coords", True)

    rows = []               # (lod, model, klasse, naam, verdieping, guid, ewkt)
    hulls = {}              # verdieping -> lijst met 2D-omtrekken
    zrange = {}             # verdieping -> lijst met (zmin, zmax) per element
    alle_hulls, z_all = [], []

    log(f"IFC openen: {args.ifc}")
    f = ifcopenshell.open(args.ifc)
    m = map_conversion(f)
    log(f"Georeferentie: {m['crs']}, oorsprong RD {m['e']:.1f}, {m['n']:.1f}, NAP {m['h']:.2f} m")
    elementen = [e for e in f.by_type("IfcElement")
                 if e.Representation is not None
                 and not any(e.is_a(k) for k in WEGLATEN + args.zonder)
                 and (not args.alleen or any(e.is_a(k) for k in args.alleen))]
    log(f"{len(elementen)} elementen, geometrie berekenen...")

    it = ifcopenshell.geom.iterator(settings, f, multiprocessing.cpu_count(), include=elementen)
    n = 0
    if it.initialize():
        while True:
            shape = it.get()
            el = f.by_id(shape.id)
            v = np.array(shape.geometry.verts, dtype=float).reshape(-1, 3)
            fi = np.array(shape.geometry.faces, dtype=int).reshape(-1, 3)
            if len(fi):
                v = naar_rd(v, m)
                tris = v[fi]
                # gedegenereerde (platte) driehoeken weglaten
                opp = np.linalg.norm(np.cross(tris[:, 1] - tris[:, 0], tris[:, 2] - tris[:, 0]), axis=1)
                tris = tris[opp > 1e-6]
                if len(tris):
                    st = verdieping(el)
                    st_naam = st.Name if st else None
                    rows.append((2, args.model, el.is_a(), el.Name, st_naam, el.GlobalId, tin_wkt(tris)))
                    if not args.alleen_detail:
                        hull = MultiPoint(v[:, :2]).convex_hull
                        if hull.geom_type == "Polygon" and hull.area > 0.01:
                            alle_hulls.append(hull)
                            if st_naam is not None:
                                hulls.setdefault(st_naam, []).append(hull)
                                zrange.setdefault(st_naam, []).append((v[:, 2].min(), v[:, 2].max()))
                        z_all.append((v[:, 2].min(), v[:, 2].max()))
            n += 1
            if n % 5000 == 0:
                log(f"  {n} elementen verwerkt")
            if not it.next():
                break
    log(f"{n} elementen verwerkt, {len(rows)} met geometrie")
    if not rows:
        sys.exit("Geen geometrie gevonden.")

    if not args.alleen_detail:
        # lod 1: per verdieping een blok. De onderkant is de typische onderkant van
        # de elementen op die verdieping; de bovenkant is de onderkant van de
        # volgende verdieping (de bovenste verdieping loopt tot het hoogste punt).
        verd = sorted(((float(np.percentile([z[0] for z in zrange[s]], 10)), s) for s in hulls))
        for i, (z0, s) in enumerate(verd):
            z1 = verd[i + 1][0] if i + 1 < len(verd) else max(z[1] for z in zrange[s])
            if z1 - z0 < 0.5:
                continue
            for p in footprint(hulls[s]):
                rows.append((1, args.model, "Verdieping", s, s, None, tin_wkt(extrudeer(p, z0, z1))))
        log(f"lod 1: {sum(1 for r in rows if r[0] == 1)} verdiepingsblokken")

        # lod 0: een blok voor het hele gebouw
        z0 = verd[0][0] if verd else min(z[0] for z in z_all)
        z1 = max(z[1] for z in z_all)
        for p in footprint(alle_hulls):
            rows.append((0, args.model, "Gebouw", "Gebouw", None, None, tin_wkt(extrudeer(p, z0, z1))))
        log(f"lod 0: {sum(1 for r in rows if r[0] == 0)} gebouwblok(ken), hoogte NAP {z0:.1f} tot {z1:.1f} m")

    # naar PostGIS (verbinding via de PG*-omgevingsvariabelen)
    t = args.tabel
    log(f"Schrijven naar {t}...")
    with psycopg.connect("") as conn, conn.cursor() as cur:
        if not args.toevoegen:
            cur.execute(f"DROP TABLE IF EXISTS {t}")
        cur.execute(f"""CREATE TABLE IF NOT EXISTS {t} (
            id serial PRIMARY KEY, lod int, model text, ifc_klasse text, naam text,
            verdieping text, guid text, geom geometry(TINZ, 4979))""")
        # eerst in RD + NAP in een tijdelijke tabel, dan omgerekend naar WGS84 met
        # hoogte boven de ellipsoide (geoide-correctie door PROJ)
        cur.execute("""CREATE TEMP TABLE invoer (lod int, model text, ifc_klasse text, naam text,
            verdieping text, guid text, geom geometry(TINZ, 7415))""")
        with cur.copy("COPY invoer (lod, model, ifc_klasse, naam, verdieping, guid, geom) FROM STDIN") as cp:
            for r in rows:
                cp.write_row(r)
        cur.execute(f"""INSERT INTO {t} (lod, model, ifc_klasse, naam, verdieping, guid, geom)
            SELECT lod, model, ifc_klasse, naam, verdieping, guid, ST_Transform(geom, 4979) FROM invoer""")
        idx = t.replace(".", "_") + "_geom_idx"
        cur.execute(f"CREATE INDEX IF NOT EXISTS {idx} ON {t} USING gist (st_centroid(st_envelope(geom)))")
        cur.execute(f"SELECT model, lod, count(*) FROM {t} GROUP BY model, lod ORDER BY model, lod")
        for model, lod, c in cur.fetchall():
            log(f"  {model}, lod {lod}: {c} objecten")
    log("Klaar.")


if __name__ == "__main__":
    main()
