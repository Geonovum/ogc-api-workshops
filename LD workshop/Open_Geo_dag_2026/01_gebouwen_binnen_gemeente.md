# Oefening 1: Gebouwen binnen een gemeente zoeken

## Doel

Zoek alle gebouwen binnen de geometrie van Utrecht.

## Wat leer je?

- GeoSPARQL gebruiken
- `geof:sfWithin`
- polygonen gebruiken
- ruimtelijke filtering

## Query

```sparql
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
PREFIX imxgeo-ext: <https://modellen.kkg.kadaster.nl/def/imxgeo-ext#>
PREFIX imxgeo: <http://modellen.geostandaarden.nl/def/imx-geo#>

SELECT ?gebouw ?wkt
WHERE {
  ?gebouw a imxgeo:Gebouw;
    imxgeo-ext:maaiveldgeometrie/geo:asWKT ?wkt .

  FILTER(
    geof:sfWithin(
      ?wkt,
      "POLYGON((5.0 52.0,5.3 52.0,5.3 52.2,5.0 52.2,5.0 52.0))"^^geo:wktLiteral
    )
  )
}
LIMIT 100
```

## Opdrachten

1. Verhoog de LIMIT.
2. Toon de resultaten op de kaart.
