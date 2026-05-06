# Oefening 2: Gebouwen dichtbij een kerk zoeken

## Doel

Vind gebouwen binnen 100 meter van een kerk.

## Wat leer je?

- afstandsfuncties
- buffer-logica
- nabijheidsanalyse

## Query

```sparql
REFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
PREFIX uom: <http://www.opengis.net/def/uom/OGC/1.0/>
PREFIX imxgeo: <http://modellen.geostandaarden.nl/def/imx-geo#>
prefix ext: <https://modellen.kkg.kadaster.nl/def/imxgeo-ext#>
SELECT ?gebouw ?kerk
WHERE {
  ?gebouw a imxgeo:Gebouw;
    geo:hasGeometry/geo:asWKT ?gebouwWKT .
  ?kerk a imxgeo:Gebouw ;
                  ext:gebouwType "kerk";
    imxgeo:bevindtZichOpPerceel/geo:hasGeometry/geo:asWKT ?kerkWKT.

  FILTER(
    geof:distance(?gebouwWKT, ?kerkWKT, uom:metre) < 100
  )
}
limit 10
```

## Opdrachten

1. Verander 100 meter naar 500 meter.
2. Sorteer op afstand.

