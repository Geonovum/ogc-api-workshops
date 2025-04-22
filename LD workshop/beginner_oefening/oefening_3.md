# Oefening 3: Verkennen van de geometrie in de Kadaster Knowledge Graph

## 1. Bevragen van geometrie en tonen op de kaart

Ga naar de volgende website:

- Kadaster SPRAQL Query Interface <https://data.kkg.kadaster.nl/sparql/>

We gaan nu de eerste geometrie bevragen die beschikbaar is in de kadaster knowledge graph.

Laten we eerst bekijken welke dingen er gebruik maken van de relatie "hasGeometry":

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX geo: <http://www.opengis.net/ont/geosparql#>

select ?s ?o where {
  ?s geo:hasGeometry ?o
} limit 15
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Welke "Subjects" kom je tegen? En welke "object"? Klik eens op de URI's om meer informatie hier over te vinden. 

Vraag: Hoe is de geometrie opgebouwd in de resultaten die je als "object" terug krijgt? 


Bevraag nu de dataset op de objecten op de asWKT beschrijving van de geometrie: 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX geo: <http://www.opengis.net/ont/geosparql#>

select ?s ?wkt where {
  ?s geo:hasGeometry/geo:asWKT ?wkt
} limit 15
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Wat is het resultaat? 

Druk op de tab "Table" en druk op de tab "Geo" en "Geo-3D". 

In de imxgeo-extensie zit ook bepaald "maaiveldgeometrie". Laten we deze bevragen met: 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX geo: <http://www.opengis.net/ont/geosparql#>

select ?s ?wkt where {
  ?s imxgeo-ext:maaiveldgeometrie/geo:asWKT ?wkt
} limit 15
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## 2. De vragen uit oefening 2 tonen op de kaart

In oefening twee zijn wij geeindigt met het bevragen van de dataset naar de kerken van voor 1101 en na 2024. 

Deze kunnen we tonen op de kaart door de geometrie van de gevonden resultaten te tonen. Dit is een combinatie van hetgeen wij hiervoor hebben gedaan. Je kunt dit zelf bouwen, of je mag gebruik maken van de code hieronder. 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
prefix imxgeo: <http://modellen.geostandaarden.nl/def/imx-geo#>
prefix imxgeo-ext: <https://modellen.kkg.kadaster.nl/def/imxgeo-ext#>
PREFIX geo: <http://www.opengis.net/ont/geosparql#>

select ?gebouw ?bouwjaar ?wkt

WHERE{{
      ?gebouw imxgeo:bouwjaar ?bouwjaar.
      FILTER(?bouwjaar < "1101"^^<http://www.w3.org/2001/XMLSchema#gYear>).
      ?gebouw imxgeo-ext:gebouwType "kerk"^^<http://www.w3.org/2001/XMLSchema#string>.
      ?gebouw imxgeo-ext:maaiveldgeometrie/geo:asWKT ?wkt.
     } 
UNION{
      ?gebouw imxgeo:bouwjaar ?bouwjaar.
      FILTER(?bouwjaar > "2023"^^<http://www.w3.org/2001/XMLSchema#gYear>).
      ?gebouw imxgeo-ext:gebouwType "kerk"^^<http://www.w3.org/2001/XMLSchema#string>.
       ?gebouw imxgeo-ext:maaiveldgeometrie/geo:asWKT ?wkt.
}}
limit 1000
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## 2. Topologische bevragingen van GeoSPARQL gebruiken: 

Met het woordenboek GeoSPARQL is het mogelijk om topologische bevragingen te doen op datasets: 

Het is bijvoorbeeld mogelijk om met de functie "geof:sfWithin" een bevraging te doen of geometrie zich binnen een gestelde waarde bevindt. In dit geval gebruiken wij de bounding box van de stad Utrecht in WKT. Probeer onderstaande querie. 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
prefix imxgeo: <http://modellen.geostandaarden.nl/def/imx-geo#>
prefix imxgeo-ext: <https://modellen.kkg.kadaster.nl/def/imxgeo-ext#>
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>

select ?gebouw ?bouwjaar ?wkt

WHERE{{
      ?gebouw imxgeo:bouwjaar ?bouwjaar.
      FILTER(?bouwjaar < "1101"^^<http://www.w3.org/2001/XMLSchema#gYear>).
      ?gebouw imxgeo-ext:gebouwType "kerk"^^<http://www.w3.org/2001/XMLSchema#string>.
      ?gebouw imxgeo-ext:maaiveldgeometrie/geo:asWKT ?wkt.
     } 
UNION{
      ?gebouw imxgeo:bouwjaar ?bouwjaar.
      FILTER(?bouwjaar > "2023"^^<http://www.w3.org/2001/XMLSchema#gYear>).
      ?gebouw imxgeo-ext:gebouwType "kerk"^^<http://www.w3.org/2001/XMLSchema#string>.
       ?gebouw imxgeo-ext:maaiveldgeometrie/geo:asWKT ?wkt.
}
FILTER (geof:sfWithin (?wkt, "POLYGON((5.0122 52.0346, 5.1828 52.0346, 5.1828 52.1426, 5.0122 52.1426, 5.0122 52.0346))"^^geo:wktLiteral))
}

limit 10
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## 3. Styling en Tooltips: 

Met SPARQL is het ook mogelijk om een kleur en tooltips mee te geven 

Kleur kan men bijvoorbeeld meegen door:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix imxgeo: <http://modellen.geostandaarden.nl/def/imx-geo#>
prefix imxgeo-ext: <https://modellen.kkg.kadaster.nl/def/imxgeo-ext#>
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>

select ?gebouw ?bouwjaar ?wkt ("green" as ?wktColor) ?result

WHERE{{
      ?gebouw imxgeo:bouwjaar ?bouwjaar.
      FILTER(?bouwjaar < "1101"^^<http://www.w3.org/2001/XMLSchema#gYear>).
      ?gebouw imxgeo-ext:gebouwType "kerk"^^<http://www.w3.org/2001/XMLSchema#string>.
      ?gebouw imxgeo-ext:maaiveldgeometrie/geo:asWKT ?wkt.
     } 
UNION{
      ?gebouw imxgeo:bouwjaar ?bouwjaar.
      FILTER(?bouwjaar > "2023"^^<http://www.w3.org/2001/XMLSchema#gYear>).
      ?gebouw imxgeo-ext:gebouwType "kerk"^^<http://www.w3.org/2001/XMLSchema#string>.
      ?gebouw imxgeo-ext:gebouwType ?gebouwtype.
      ?gebouw imxgeo-ext:maaiveldgeometrie/geo:asWKT ?wkt.
  }      
FILTER (geof:sfWithin (?wkt, "POLYGON((5.0122 52.0346, 5.1828 52.0346, 5.1828 52.1426, 5.0122 52.1426, 5.0122 52.0346))"^^geo:wktLiteral)).
}
limit 10

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


TODO: https://www.dbpedia.org/resources/knowledge-graphs/

https://dbpedia.org/snorql/

https://dbpedia.org/snorql/?query=SELECT%20?name%20?birth%20?death%20?person%20WHERE%20{%20%20%20%20%20%20?person%20dbo:birthPlace%20:Berlin%20.%20%20%20%20%20%20?person%20dbo:birthDate%20?birth%20.%20%20%20%20%20%20?person%20foaf:name%20?name%20.%20%20%20%20%20%20?person%20dbo:deathDate%20?death%20.%20%20%20%20%20%20FILTER%20(?birth%20%3C%20%221900-01-01%22^^xsd:date)%20.%20}%20ORDER%20BY%20?name
