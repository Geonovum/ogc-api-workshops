# Oefening 1: Verkennen van de Kadaster Knowledge Graph

## 1. Verken het linked data model van het kadaster

Ga naar de volgende website en bekijk de beschikbare data:

- Kadaster Knowledge Graph <https://data.labs.kadaster.nl/kadaster/kkg>

Welke datasets zijn beschikbaar en volgens welke woordenboeken zijn deze opgesteld? 

-   **Antwoord**: De BAG, BGT, BRT, BRK, PB en CBS zijn als linked data sets opgesteld. 
Deze zijn volgens GeoSPARQL, NEN3610, IMX-Geo, SHACL, PROV, RDF, RDFS, SKOS (W3C) opgesteld. 

## 2.Klik op de tab "Triples" 

Er worden verschillende kolommen getoond. 

Subject, Predicate en Object zijn de onderdelen van een triple. Graph toont in welke kennisgraaf deze triple staat. 

Typ in het invulveld onder "Object" de url: https://bag.basisregistraties.overheid.nl/def/bag# 

Welke concepten zijn er beschikbaar in deze kennisgraaf?  

-   **Antwoord**: Nummeraanduiding, Openbareruimte, Pand, Verblijfsobject, Woonplaats

Typ in het invulveld onder "Subject" de PREFIX: imxgeo: 

Wie heeft dit model gemaakt? 

Haal het "Subject" weg en typ onder "Object" de term: imxgeo:Adres

Klik op de URL van een van de triples die als resultaat terug komen.

Welke andere predicates en objects zijn gekoppeld aan iets dat van het type Adres is? 

## 2. Filter de triples op bepaalde waarden

Haal de waarde in de kolom "Object" weg en typ onder "Predicate" de term: imxgeo:Bouwjaar

Voeg onder Object de waarde: "2024"^^http://www.w3.org/2001/XMLSchema#gYear in. 

Zijn er ook gebouwen uit het jaar "1100"? 

Wat voor soort gebouwen zijn dit? 

Kan je op meerdere waarden filteren? 

-   **Antwoord**: Nee, dit kan niet in deze omgeving. Dit kan wel in de bevraagomgeving van deze dataset (SPARQL)

## 3. Bekijk het schema 

Klik op de tab "Insights" en klik op "Schema". 

Filter op imxgeo:Gebouw. Komt dit bekend voor? 

![alt text](media/58a35c62bb8e456ebd0b9fdb7850878f.png)

Welke relaties (predicates) zijn er mogelijk vanuit imxgeo:Gebouw? 

## 3. Bekijk de verschillende kennisgrafen 

Klik op de tab "Graphs"

Welke graaf bevat de meeste statements (triples)?

-   **Antwoord**: De kennisgraaf graph:ip_adres

Klik op het dropdown teken. Welke gegevens zijn zijn er bij Adres in deze kennisgraaf aanwezig? 

Zet de filter van het number of statements onder de 5.000. Wat valt op? 

