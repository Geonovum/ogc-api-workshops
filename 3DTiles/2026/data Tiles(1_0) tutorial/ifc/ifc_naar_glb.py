#!/usr/bin/env python3
"""
IFC -> GLB (glTF), om als los 3D-model in Cesium te plaatsen.

Ruimtes (IfcSpace) en sparingen (IfcOpeningElement) worden weggelaten.
De oorsprong van het GLB-model is de oorsprong van de IFC. Is de IFC
gegeorefereerd (IfcMapConversion naar RD), dan print het script ook de
Cesium-code met de juiste lengte- en breedtegraad en hoogte.

Gebruik (in de ifc-container):
  ifc_naar_glb.py model.ifc               -> model.glb
  ifc_naar_glb.py model.ifc -o gebouw.glb
"""
import argparse
import math
import multiprocessing
import os
import sys
import time

import ifcopenshell
import ifcopenshell.geom

WEGLATEN = ["IfcSpace", "IfcOpeningElement"]


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def locatie(f):
    """Oorsprong van de IFC in RD + NAP, en omgerekend naar WGS84 (via PostGIS)."""
    mcs = f.by_type("IfcMapConversion")
    if not mcs:
        return None
    mc = mcs[0]
    e, n, h = mc.Eastings, mc.Northings, mc.OrthogonalHeight or 0.0
    a = mc.XAxisAbscissa if mc.XAxisAbscissa is not None else 1.0
    o = mc.XAxisOrdinate if mc.XAxisOrdinate is not None else 0.0
    rotatie = math.degrees(math.atan2(o, a))
    res = dict(crs=mc.TargetCRS.Name if mc.TargetCRS else "?", e=e, n=n, h=h, rotatie=rotatie)
    if "28992" in res["crs"] and os.environ.get("PGHOST"):
        try:
            import psycopg
            with psycopg.connect("") as conn:
                lon, lat, hell = conn.execute(
                    "SELECT ST_X(p), ST_Y(p), ST_Z(p) FROM "
                    "(SELECT ST_Transform(ST_SetSRID(ST_MakePoint(%s, %s, %s), 7415), 4979) p) q",
                    (e, n, h)).fetchone()
            res.update(lon=lon, lat=lat, hell=hell)
        except Exception as ex:  # database niet bereikbaar: alleen RD tonen
            log(f"Omrekenen naar WGS84 lukte niet ({ex}).")
    return res


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ifc", help="IFC-bestand")
    ap.add_argument("-o", "--output", help="GLB-bestand (standaard: naam van de IFC met .glb)")
    args = ap.parse_args()
    uit = args.output or os.path.splitext(args.ifc)[0] + ".glb"

    log(f"IFC openen: {args.ifc}")
    f = ifcopenshell.open(args.ifc)

    settings = ifcopenshell.geom.settings()
    settings.set("use-world-coords", True)   # alle elementen in een assenstelsel
    settings.set("y-up", True)               # glTF gebruikt Y als 'omhoog'
    settings.set("use-element-guids", True)  # elementen herkenbaar in het GLB

    weg = [e for k in WEGLATEN for e in f.by_type(k)]
    ser = ifcopenshell.geom.serializers.glb(uit, settings)
    ser.setFile(f)
    ser.writeHeader()
    it = ifcopenshell.geom.iterator(settings, f, multiprocessing.cpu_count(), exclude=weg)
    n = 0
    log("Geometrie berekenen en wegschrijven...")
    if it.initialize():
        while True:
            ser.write(it.get())
            n += 1
            if n % 5000 == 0:
                log(f"  {n} elementen")
            if not it.next():
                break
    ser.finalize()
    log(f"Klaar: {n} elementen -> {uit} ({os.path.getsize(uit) / 1e6:.1f} MB)")

    loc = locatie(f)
    if loc is None:
        print("\nDe IFC heeft geen georeferentie (IfcMapConversion): kies zelf een locatie in Cesium.")
        return
    print(f"\nGeoreferentie: {loc['crs']}, oorsprong RD {loc['e']:.2f}, {loc['n']:.2f}, NAP {loc['h']:.2f} m")
    if "lon" in loc:
        print("Plaats het model in cesium-viewer.html met:\n")
        print("viewer.entities.add({")
        print(f"  position: Cesium.Cartesian3.fromDegrees({loc['lon']:.7f}, {loc['lat']:.7f}, {loc['hell']:.2f}),")
        if abs(loc["rotatie"]) > 0.01:
            print("  orientation: Cesium.Transforms.headingPitchRollQuaternion(")
            print(f"    Cesium.Cartesian3.fromDegrees({loc['lon']:.7f}, {loc['lat']:.7f}, {loc['hell']:.2f}),")
            print(f"    new Cesium.HeadingPitchRoll(Cesium.Math.toRadians({-loc['rotatie']:.3f}), 0, 0)),")
        print("  model: {")
        print(f'    uri: "{os.path.basename(uit)}",')
        print("  },")
        print("});")
        print(f"\nDe hoogte {loc['hell']:.2f} m is NAP {loc['h']:.2f} m omgerekend naar hoogte boven de ellipsoide.")


if __name__ == "__main__":
    main()
