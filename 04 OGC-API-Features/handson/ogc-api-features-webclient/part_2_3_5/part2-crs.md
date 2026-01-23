# Part 2 — CRS (Coördinaatreferentiesystemen)

## Doel
Korte theorie over CRS en hands-on oefeningen waarmee deelnemers leren:
- welke CRS een API ondersteunt,
- hoe je requests in verschillende CRS doet,
- wanneer reprojection client- of server-side plaatsvindt.

## Theorie (kort)
- Wat is een CRS; verschil tussen geographic en projected.
- EPSG-codes en axis-order (bijv. `EPSG:4326` vs `EPSG:3857` vs nationale EPSG-codes).
- Waar in OGC API Features je CRS vindt: collectie metadata (`/collections` en `/collections/{id}` — links/`crs`/`supportedCRS`).
- Default / native CRS van de server en hoe de server reprojection aanbiedt.
- Effect op `bbox` en feature-coördinaten; precisie en datumtransformaties.

## Oefeningen

1) Verkenning
- Open de landing page van de API (bijv. PDOK demo) en ga naar `/collections`.
- Vind voor een collectie welke CRS worden ondersteund en noteer de EPSG-codes.

2) Request in andere CRS
- Gebruik de Swagger UI of browser en vraag `GET /collections/{id}/items?crs=EPSG:4326` (of de parameter zoals beschreven in de OpenAPI spec van de server).
- Vergelijk de geometrieën met het native CRS-response.

3) BBOX in een niet-native CRS
- Maak twee bbox-requests (een in native CRS, een in EPSG:4326 of EPSG:28992). Vergelijk aantallen features en coördinaten.

4) Client-side reprojection (voorbeeld)
- Open `crs-demo.html` in je browser. Dit kleine script haalt features op in het native CRS en reprojecteert naar EPSG:3857/EPSG:4326 met `proj4`.
- Pas de API-base URL in het script aan naar je target API en test.

5) QGIS-check (optioneel)
- Laad een GeoJSON-response als laag in QGIS en wissel de project-CRS; controleer of geometrieën correct verschijnen.

