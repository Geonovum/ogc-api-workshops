# Part 3 — Filtering

## Doel
Deelnemers leren hoe ze features kunnen filteren via OGC API Features Part 3: property-filters, spatial en temporal filters, en het gebruik van `queryables`.

## Theorie (kort)
- Basisquery-parameters: `bbox`, `datetime`, `limit`, `offset`, `sortby`.
- `queryables` endpoint: welke properties kunnen gefilterd worden en welke types hebben ze.
- Filtertalen: CQL2 (tekst/JSON) of implementatie-specifieke varianten; logische operatoren en spatial predicates.
- Combinatie van filters (AND/OR) en performance/security overwegingen.

## Oefeningen

1) Verken `queryables`
- Open `/collections/{id}/queryables` en noteer 3 velden die als queryable beschikbaar zijn.

2) Simpele property-filter
- Bouw in Swagger UI of de browser een request dat filtert op een property, bijv. `type='bak'` of `status='actueel'`.
- Controleer de JSON-respons en noteer het aantal resultaten.

3) Spatial + temporal combinatie
- Vraag items op met `bbox=...` en `datetime=YYYY-MM-DD/YYYY-MM-DD` en vergelijk resultaten met alleen bbox.

4) Filter playground (examples/filter-playground.html)
- Open de voorbeeldpagina, vul property/waarde en bbox in en druk op "Query". De pagina bouwt een filter-parameter en toont de resultaten.
- Tip: controleer de OpenAPI van de server om te zien hoe je filters moet doorgeven; pas de parameternaam aan op de pagina indien nodig.

5) Complexere expressies
- Probeer een gecombineerde expressie (bijv. `population > 1000 AND landuse = 'residential'`) met de server-ondersteunde syntax.

---
