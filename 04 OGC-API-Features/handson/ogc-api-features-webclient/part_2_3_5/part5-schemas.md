# Part 5 — Schemas (JSON Schema)

## Doel
Inzicht geven in het gebruik van JSON Schema binnen OGC API Features: waar schemas staan, hoe ze eigenschappen en validatie beschrijven, en hoe je ze praktisch gebruikt (validatie, formuliergeneratie).

## Theorie (kort)
- JSON Schema: types, `required`, `properties`, `format`.
- Waar schema's in OGC API Features te vinden zijn: link in `/collections/{id}` of `/collections/{id}/items/schema`.
- Verschil tussen OpenAPI en collectie-schema's; waarom schema's belangrijk zijn voor clients.

## Oefeningen

1) Vind het schema
- Open `/collections/{id}` en zoek de link naar het collectie-schema. Noteer `required` properties.

2) Valideer een feature
- Open `schema-validate.html`. Vul de URL van een collectie-schema en een feature-URL (of gebruik `/collections/{id}/items?limit=1`).
- Druk op "Validate" en bekijk of het item voldoet aan het schema.

3) Formuliergeneratie
- Gebruik de schema-eigenschappen om op papier of in een eenvoudige HTML-form-generator een form te maken voor het aanmaken van een nieuw feature (mock; niet per se POST uitvoeren).

