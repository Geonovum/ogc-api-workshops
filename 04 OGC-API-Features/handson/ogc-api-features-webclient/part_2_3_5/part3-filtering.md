# Part 3 — Filtering

## Doel
leren hoe je features kan filteren via OGC API Features Part 3: property-filters, spatial en temporal filters, en het gebruik van `queryables`.

## Theorie (kort)
- Basisquery-parameters: `bbox`, `datetime`, `limit`, `offset`, `sortby`.
- `queryables` endpoint: welke properties kunnen gefilterd worden en welke types hebben ze.
- Filtertalen: CQL2 (tekst/JSON) of implementatie-specifieke varianten; logische operatoren en spatial predicates.
- Combinatie van filters (AND/OR) en performance/security overwegingen.

__NB__ PDOK is bezig Part 3 te implementeren, dus niet alle filter functionaliteit werkt mogelijk op de PDOK API's.
Probeer daarom een andere service om de opdrachten uit te voeren als het niet werkt met die van PDOK. Bijvoorbeeld: https://apitestbed.geonovum.nl/adr_pygeoapi/v1/


## Oefeningen

1) Verken de `queryables` in de verschillende collecties:
- Open `/collections/{id}/queryables` en noteer 3 velden die als queryable beschikbaar zijn.

2) Simpele property-filter
- Bouw in Swagger UI of de browser een request dat filtert op een property.
- Controleer de JSON-respons en noteer het aantal resultaten.

3) Spatial + temporal combinatie
- Vraag items op met `bbox=...` en `datetime=YYYY-MM-DD/YYYY-MM-DD` en vergelijk resultaten met alleen bbox.

4) Filter playground ([filter-playground.html](https://github.com/Geonovum/ogc-api-workshops/blob/main/04%20OGC-API-Features/handson/ogc-api-features-webclient/part_2_3_5/filter-playground.html))
- Open de voorbeeldpagina, vul property/waarde en bbox in en druk op "Query". De pagina bouwt een filter-parameter en toont de resultaten.
- Tip: controleer de OpenAPI van de server om te zien hoe je filters moet doorgeven; pas de parameternaam aan op de pagina indien nodig.

5) Complexere expressies
- Probeer een gecombineerde expressie (bijv. `population > 1000 AND landuse = 'residential'`) met de server-ondersteunde syntax.:
https://gs-main.geosolutionsgroup.com/geoserver/ogc/features/v1/collections/topp:states/items?filter=PERSONS%3E6660000%20AND%20HOUSHOLD%3C4440000

6) ruimtelijke filters
- probeer een ruimtelijk filter:
https://gs-main.geosolutionsgroup.com/geoserver/ogc/features/v1/collections/topp:states/items?filter=s_intersects(the_geom,POLYGON((-75%2035,-80%2037,-77%2051,-75%2035)))
