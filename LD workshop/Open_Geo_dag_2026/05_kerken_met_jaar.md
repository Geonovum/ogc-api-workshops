# Oefening 5: Kerken op de kaart tonen met kleurcodes

## Doel
Visualisatie maken.

## Wat leer je?
- styling
- thematische kaarten
- dynamische kleuren

## Query

```sparql
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
PREFIX uom: <http://www.opengis.net/def/uom/OGC/1.0/>
PREFIX imxgeo: <http://modellen.geostandaarden.nl/def/imx-geo#>
PREFIX bif: <http://www.openlinksw.com/schemas/bif#>
PREFIX imxgeo-ext: <https://modellen.kkg.kadaster.nl/def/imxgeo-ext#>
SELECT ?kerk ?wkt
       ("red" as ?wktColor)
WHERE {
  ?kerk a imxgeo:Gebouw ;
        ext:gebouwType "kerk";
    imxgeo:bevindtZichOpPerceel/geo:hasGeometry/geo:asWKT ?kerkWKT.
}
LIMIT 100
```

## Opdrachten
1. Maak oude kerken rood. (Zoek voor imxgeo:bouwjaar)
2. Maak nieuwe kerken groen. (bind specifieke waarde van bouwjaar met specifieke kleur)