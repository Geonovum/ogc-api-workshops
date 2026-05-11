# Oefening 2: Spoorbanen dichtbij specifieke punt

## Doel

Vind spoorbanen binnen 10000 meter van een punt.

## Wat leer je?

- afstandsfuncties
- buffer-logica
- nabijheidsanalyse

## Query

```sparql
PREFIX imx: <http://modellen.geostandaarden.nl/def/imx-geo#>
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX uom: <http://www.opengis.net/def/uom/OGC/1.0/>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>

select distinct ?geo_wgs84 ?wegdeel_uri
where {
  BIND("POINT(5.0672624 52.07812164)"^^geo:wktLiteral AS ?geo_locatie) 
  
  ?wegdeel_uri a imx:Weg;  
                 imx:functie "spoorbaan";
                 geo:hasGeometry/geo:asWKT ?geo_wgs84.
  
  BIND(geof:distance(?geo_locatie, ?geo_wgs84, uom:metre) as ?afstand) 

  FILTER (?afstand < 10000)
  
}
```

## Opdrachten

1. Verander 10000 meter naar 5000 meter.
2. Verander functie bv aan "rijbaan autosnelweg".

