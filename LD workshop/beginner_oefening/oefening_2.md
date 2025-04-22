# Oefening 2: Bevragen van de Kadaster Knowledge Graph met SPARQL

## 1. Een eerste SPARQL Query 

Ga naar de volgende website en druk op de tab SPARQL:

- Kadaster Knowledge Graph <https://data.labs.kadaster.nl/kadaster/kkg>

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
select * where {
  ?s ?p ?o.
} limit 15
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

![alt text](media/bfbfba94d18c4723a7f965e79d3cd30b.png)

Druk op Execute Query en bekijk het resultaat. 

waar staan ?s ?p en ?o voor in deze query? 

-   **Antwoord**: Subject Predicate en Object 

verander de limit naar een ander (klein) getal en run de query opnieuw. 

## 2. De kennisgraaf gebouwen met SPARQL bevragen op bouwjaar

Type in plaats van ?p imxgeo:bouwjaar. Wat gebeurt er? 

Run de Query. 

Type de volgende Query. De "*" veranderen we in ? s

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
prefix imxgeo: <http://modellen.geostandaarden.nl/def/imx-geo#>
select ?s {
  ?s imxgeo:bouwjaar ?o.
} limit 10
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

run de query. Wat gebeurt er? 

Door achter select de "?s" terug te veranderen in "*" of in "?s ?p ?o" worden meerdere resultaten in kolom getoond. 

Laten we de kadaster kennisgraaf bevragen op de dingen die een bouwjaar van 2024 hebben met onderstaande query: 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
prefix imxgeo: <http://modellen.geostandaarden.nl/def/imx-geo#>
select *{
  ?s imxgeo:bouwjaar "2024"^^<http://www.w3.org/2001/XMLSchema#gYear>.
} limit 10
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Probeer het bouwjaar eens in "1100" te veranderen. Komen de resultaten je bekend voor? 

Zet de limit naar 100. Hoeveel gebouwen zijn er van het bouwjaar 1100? 

## 3. De kennisgraaf gebouwen met SPARQL bevragen op meerdere aspecten
Een query kan op meerdere aspecten zoeken. Op basis van onderstaande query worden dingen van het bouwjaar "1100" en het gebouwtype "kerk" gezocht. 
Zie dat nu ook de begrippen uit het model imxgeo-ext wordt bevraagd. 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
prefix imxgeo: <http://modellen.geostandaarden.nl/def/imx-geo#>
prefix imxgeo-ext: <https://modellen.kkg.kadaster.nl/def/imxgeo-ext#>

select ?gebouw {
      ?gebouw imxgeo:bouwjaar "1100"^^<http://www.w3.org/2001/XMLSchema#gYear>.
      ?gebouw imxgeo-ext:gebouwType "kerk"^^<http://www.w3.org/2001/XMLSchema#string>.
} limit 100
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## 4. De kennisgraaf gebouwen met SPARQL bevragen op meerdere aspecten, filteren en samenvoegen 
Met SPARQL kan je met een FILTER ook rekenen en daarop filteren. 

Met onderstaande query wordt het volgende gevraagd aan een dataset: 

Selecteer een gebouw met een bouwjaar, en dat bouwjaar dient onder 1101 als jaartal te liggen. Het gebouw dient ook van het type kerk te zijn.  

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
prefix imxgeo: <http://modellen.geostandaarden.nl/def/imx-geo#>
prefix imxgeo-ext: <https://modellen.kkg.kadaster.nl/def/imxgeo-ext#>

select ?gebouw ?bouwjaar{
      ?gebouw imxgeo:bouwjaar ?bouwjaar.
      FILTER(?bouwjaar < "1101"^^<http://www.w3.org/2001/XMLSchema#gYear>).
      ?gebouw imxgeo-ext:gebouwType "kerk"^^<http://www.w3.org/2001/XMLSchema#string>.
} limit 100
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Met de functie UNION kunnen meerdere resultaten worden samengevoegd. 

Wat denk je dat onderstaande SPARQL Query doet? 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
prefix imxgeo: <http://modellen.geostandaarden.nl/def/imx-geo#>
prefix imxgeo-ext: <https://modellen.kkg.kadaster.nl/def/imxgeo-ext#>

select ?gebouw ?bouwjaar

WHERE{
      ?gebouw imxgeo:bouwjaar ?bouwjaar.
      FILTER(?bouwjaar < "1101"^^<http://www.w3.org/2001/XMLSchema#gYear>).
      ?gebouw imxgeo-ext:gebouwType "kerk"^^<http://www.w3.org/2001/XMLSchema#string>.
     } 
UNION{
      ?gebouw imxgeo:bouwjaar ?bouwjaar.
      FILTER(?bouwjaar > "2023"^^<http://www.w3.org/2001/XMLSchema#gYear>).
      ?gebouw imxgeo-ext:gebouwType "kerk"^^<http://www.w3.org/2001/XMLSchema#string>.
     } 
limit 1000
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Probeer deze uit in de SPARQL Query interface. 

Er zijn nog veel andere mogelijkheden met SPARQL. Deze zijn beschreven op: https://www.w3.org/TR/sparql11-query/

