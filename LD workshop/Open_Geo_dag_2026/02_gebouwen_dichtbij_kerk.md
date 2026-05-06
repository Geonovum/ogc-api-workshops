# Oefening 2: Gebouwen dichtbij een kerk zoeken

## Doel

Vind gebouwen binnen 100 meter van een kerk.

## Wat leer je?

- afstandsfuncties
- buffer-logica
- nabijheidsanalyse

## Query

```sparql
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
PREFIX uom: <http://www.opengis.net/def/uom/OGC/1.0/>
PREFIX imxgeo: <http://modellen.geostandaarden.nl/def/imx-geo#>
PREFIX ext: <https://modellen.kkg.kadaster.nl/def/imxgeo-ext#>
PREFIX bif: <http://www.openlinksw.com/schemas/bif#>
PREFIX imxgeo-ext: <https://modellen.kkg.kadaster.nl/def/imxgeo-ext#>

SELECT ?puntWKT ?kerkWKT
WHERE {
  ?gebouw a imxgeo:Gebouw;
    imxgeo:heeftAlsAdres/geo:hasGeometry/geo:asWKT ?puntWKT.
  ?kerk a imxgeo:Gebouw ;
                  ext:gebouwType "kerk";
    imxgeo:bevindtZichOpPerceel/geo:hasGeometry/geo:asWKT ?kerkWKT.
 
   bind(geof:distance(?puntWKT, ?kerkWKT, uom:meter) as ?distance)
filter (?distance<100000)
}
limit 100
```

## Opdrachten

1. Verander 100 meter naar 500 meter.
2. Sorteer op afstand.

