# Oefening 1: Verkennen van de beschikbare Styles via de PDOK interface

## 1. Verken de Styles voor BAG, BGT en BRT TOP10NL

Ga naar de volgende PDOK API eindpunten en bekijk de beschikbare stijlen:

-   BAG: <https://api.pdok.nl/lv/bag/ogc/v1/>

-   BGT: <https://api.pdok.nl/lv/bgt/ogc/v1/>

-   BRT TOP10NL: <https://api.pdok.nl/brt/top10nl/ogc/v1/>

## 2. Vergelijk de rendering van de BAG voor de tilesets 'NetherlandsRDNewQuad' en 'WebMercatorQuad'

Wat valt op bij het vergelijken van de rendering van de symbolen en labels
tussen deze twee tilesets?

-   **Antwoord**: De plaatsing van de symbolen en labels kan licht verschillen
    tussen de twee tilesets, wat te maken heeft met de projectie en
    coördinatenstelsels (RD en Web Mercator). Dit heeft invloed op de
    positionering en weergave van objecten op de kaart.

## 3. Bekijk de stijl in zowel HTML als JSON formaat

Gebruik de volgende links om de stijl van de BAG te bekijken in HTML en JSON:

-   HTML:
    <https://api.pdok.nl/lv/bag/ogc/v1/styles/bag_standaardvisualisatie__webmercatorquad?f=html>

-   JSON:
    <https://api.pdok.nl/lv/bag/ogc/v1/styles/bag_standaardvisualisatie__webmercatorquad?f=json>

## 4. Legenda en statussen van de Panden in de BAG

In de HTML weergave zie je verschillende stijlen voor de statussen van de Panden
in de BAG. Kijk goed naar de JSON-weergave en vergelijk de representatie van
deze stijlen.

-   Het is belangrijk om deze details goed door te nemen, omdat we later zelf
    stijlen gaan beheren en toepassen.
