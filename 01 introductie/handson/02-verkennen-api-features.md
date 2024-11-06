# Verkennen van OGC API Features

Bij deze oefeningen gaan we dieper in op het verkennen van de OGC API Features
van de BGT. We zullen de demo van PDOK gebruiken om praktische vaardigheden te
ontwikkelen voor het navigeren en filteren van geografische data.

## BGT OGC API Features

Ga naar de demo van PDOK die sinds 11 maart 2024 beschikbaar is:
<https://api.pdok.nl/lv/bgt/ogc/v1/>. Je komt de terecht op de landing
page.

![Afbeelding met tekst, schermopname, Website, Webpagina Automatisch
gegenereerde beschrijving](media/32b7442861e1e387e715acac2c4f755d.png)

### Conformance

Ga naar de Conformance sectie.

-   Wat valt je op aan de Conformance-sectie in vergelijking met de conformance
    van de Vector Tiles?

### Collecties

Bekijk de beschikbare feature collecties onder het kopje "Collecties" op de
landing page: <https://api.pdok.nl/lv/bgt/ogc/v1/collections> .

-   Tot welke datum zijn deze feature collecties bijgewerkt?

Open de collectie "Bak" en bekijk de beschikbare informatie.

![Afbeelding met tekst, schermopname, kaart, software Automatisch gegenereerde
beschrijving](media/0e469c9e1a4c87d242cd8a9e95e62146.png)

-   In hoeveel coördinatenreferentiesystemen zijn de features van de collectie Bak beschikbaar?

-   In welke formaten worden de features beschikbaar gesteld?

Klik op "Blader door Features" binnen de "Bak" collectie.

-   Hoeveel objectversies zijn er van het eerste object dat voorkomt in de
    lijst?

-   Wat is het type van feature van het eerste item?

Leer hoe features gefilterd kunnen worden op datum en ID.

-   Op welke datum werd het feature met LokaalID
    G0518.08d6e6ee5822653ae0502a0a313c2ff8 in de LV opgenomen?

Vind de begindatum van het oudste "Bak" feature door terug te gaan in de
tijd.

-   Wat is het begindatum van het ‘oudste’ Bak feature?

*Hint! Ga zo’n 16 jaar terug in de tijd.*

### Open API Specificaties

Verken de OpenAPI Specificaties van BGT OAF via de Swagger UI en vind het
endpoint.

-   Wat is het endpoint van deze API?

Leer hoe je features binnen een bounding box kunt opvragen.

-   Hoe kun je features binnen een bounding box opvragen via deze API?

*Hint! Gebruik als bounding box bijvoorbeeld*

*MinX (West): 103500*

*MinY (Zuid): 446000*

*MaxX (Oost): 107000*

*MaxY (Noord): 448500*

*Dus: 103500, 446000, 107000, 448500*

*In het coördinatenreferentiesysteem WGS84 zijn als volgt:*

*- Minimale breedtegraad (Latitude, MinY): Ongeveer 51.9947 graden*

*- Minimale lengtegraad (Longitude, MinX): Ongeveer 4.6915 graden*

*- Maximale breedtegraad (Latitude, MaxY): Ongeveer 52.0174 graden*

*- Maximale lengtegraad (Longitude, MaxX): Ongeveer 4.7602 graden.*
