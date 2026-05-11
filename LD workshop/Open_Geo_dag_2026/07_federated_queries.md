# Oefening 7: Federated query met KKG, CBS en GeoSPARQL

## Doel

Combineer geo-data uit verschillende SPARQL-endpoints met behulp van een federated query (`SERVICE`).

In deze oefening combineer je:

- een rioolgebied uit de GWSW-dataset;
- buurten uit het KKG;
- CBS-kerncijfers.

Daarna visualiseer je de resultaten met een `geoLabel`.

## Wat leer je?

- federated queries (`SERVICE`)
- combineren van meerdere datasets
- GeoSPARQL ruimtelijke functies
- `bif:st_intersects`
- HTML labels genereren met `geoLabel`
- werken met CBS-gegevens

## Query

```sparql
prefix imxgeo: <http://modellen.geostandaarden.nl/def/imx-geo#>
prefix geo: <http://www.opengis.net/ont/geosparql#>
prefix gwsw: <http://data.gwsw.nl/1.4/totaal/>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix bif: <http://www.openlinksw.com/schemas/bif#>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix imxgeo-ext: <https://modellen.kkg.kadaster.nl/def/imxgeo-ext#>
prefix cbs: <https://modellen.kkg.kadaster.nl/cbs/wijken-buurten/def/kerncijfers#>

select distinct 
  ?buurtGeo 
  (strdt(concat('<h3><a href="',str(?buurt),'" target="_blank">',str(?buurtNaam),'</a></h3><p>Aantal inwoners: ',str(?aantalInwoners),'</p><p>Bevolkingsdichtheid: ',str(?bevolkingsdichtheid),' per sqkm</p><p>Land oppervlakte in ha: ',str(?oppervlakteLand),'</p><p>Water oppervlakte in ha: ',str(?oppervlakteWater),'</p>'),rdf:HTML) as ?buurtGeoLabel)
  
  where {
    
    { service <https://sparql.gwsw.nl/repositories/TestDatastory> {

    select ?bg_wkt  {
    <http://sparql.gwsw.nl/bim/juinen#Rioleringsgebied_1>
        a gwsw:Rioleringsgebied ;
        rdfs:label ?gebiedslabel ;
        gwsw:hasAspect ?ori . 
    ?ori a gwsw:Gebiedsorientatie ;
        gwsw:hasAspect ?bg . 
    ?bg a gwsw:Buitengrens ;
        geo:asWKT ?bg_wkt .      
    }
    }
  }

    
  { ?buurt
      a imxgeo:Buurt ;
      imxgeo:naam ?buurtNaam ;
      geo:hasGeometry/geo:asWKT ?buurtGeo .

    filter(bif:st_intersects(?buurtGeo, ?bg_wkt))

  ?cbsRegio 
    imxgeo-ext:regio ?buurt ;
    cbs:aantal_inwoners ?aantalInwoners ;
    cbs:bevolkingsdichtheid_inwoners_per_km2 ?bevolkingsdichtheid ;
    cbs:oppervlakte_land_in_ha ?oppervlakteLand ;
    cbs:oppervlakte_water_in_ha ?oppervlakteWater . 
    
  }
  
}
```

## Opdrachten
Voeg extra CBS-gegevens toe aan het geoLabel, bijvoorbeeld:
 - oppervlakte land;
 - oppervlakte water;
 - gemiddeld inkomen.

Maak een eenvoudiger geoLabel met alleen:
 - buurtnaam;
- aantal inwoners.

Voeg een link toe naar de URI van de buurt.

Verander bif:st_intersects naar:
- bif:st_contains;
- bif:st_within.

Gebruik een ander rioolgebied uit de GWSW-dataset.

## Extra uitdaging

Maak een label met kleuren in HTML:

<h3 style="color:darkblue">Buurtnaam</h3>
<p style="color:green">Aantal inwoners: 1200</p>

Of voeg tabellen toe:

<table border="1">
<tr><th>Kenmerk</th><th>Waarde</th></tr>
<tr><td>Inwoners</td><td>1200</td></tr>
</table>