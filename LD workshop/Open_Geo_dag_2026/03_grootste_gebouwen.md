# Oefening 3: Grootste gebouwen zoeken

## Doel
Zoek gebouwen met het grootste oppervlak.

## Wat leer je?
- geometrische berekeningen
- sorteren
- `ORDER BY`

## Query

```sparql
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
prefix imxgeo: <http://modellen.geostandaarden.nl/def/imx-geo#>
prefix imxgeo-ext: <https://modellen.kkg.kadaster.nl/def/imxgeo-ext#>

SELECT ?gebouw ?wkt ?oppervlakte  
WHERE {
  ?gebouw a imxgeo:Gebouw;
    imxgeo-ext:maaiveldgeometrie/geo:asWKT ?wkt ;
    imxgeo:bevindtZichOpPerceel/geo:hasMetricArea ?oppervlakte.
}

LIMIT 10
```

## Opdrachten
1. Zoek de kleinste gebouwen.
2. Voeg gebouwtype toe.