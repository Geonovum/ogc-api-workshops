# Inleiding op de Oefeningen

In deze workshop gaan we aan de slag met OGC API Styles, waarmee we werken met vector tiles en stijlen via API's. We zullen verschillende aspecten van de PDOK API's verkennen, inclusief het laden van kaartlagen met stijlen, het vergelijken van renderingformaten en het beheren van eigen stijlen in tools zoals QGIS en Maplibre Mapnutik.

De oefeningen zijn hands-on en gericht op praktische toepassingen, zodat je niet alleen de theorie begrijpt, maar ook daadwerkelijk met de technieken aan de slag kunt. We starten met het verkennen van de beschikbare stijlen voor belangrijke datasets zoals BAG (Basisregistratie Adressen en Gebouwen), BGT (Basisregistratie Grootschalige Topografie) en BRT TOP10NL (Basisregistratie Topografie), en werken vervolgens verder met het aanpassen en laden van eigen stijlen.

Deze sessie biedt je de gelegenheid om vertrouwd te raken met de OGC API's en hoe je stijlen kunt beheren en toepassen voor vector tiles visualisaties.

Laten we nu beginnen met de eerste oefening!

# Oefening 1: Verkennen van de beschikbare Styles via de PDOK interface

## 1. Verken de Styles voor BAG, BGT en BRT TOP10NL
Ga naar de volgende PDOK API eindpunten en bekijk de beschikbare stijlen:
- BAG: [https://api.pdok.nl/lv/bag/ogc/v1/](https://api.pdok.nl/lv/bag/ogc/v1/)
- BGT: [https://api.pdok.nl/lv/bgt/ogc/v1/](https://api.pdok.nl/lv/bgt/ogc/v1/)
- BRT TOP10NL: [https://api.pdok.nl/brt/top10nl/ogc/v1/](https://api.pdok.nl/brt/top10nl/ogc/v1/)

## 2. Vergelijk de rendering van de BAG voor de tilesets 'NetherlandsRDNewQuad' en 'WebMercatorQuad'
Wat valt op bij het vergelijken van de rendering van de symbolen en labels tussen deze twee tilesets?
- **Antwoord**: De plaatsing van de symbolen en labels kan licht verschillen tussen de twee tilesets, wat te maken heeft met de projectie en coördinatenstelsels (RD en Web Mercator). Dit heeft invloed op de positionering en weergave van objecten op de kaart.

## 3. Bekijk de stijl in zowel HTML als JSON formaat
Gebruik de volgende links om de stijl van de BAG te bekijken in HTML en JSON:
- HTML: [https://api.pdok.nl/lv/bag/ogc/v1/styles/bag_standaardvisualisatie__webmercatorquad?f=html](https://api.pdok.nl/lv/bag/ogc/v1/styles/bag_standaardvisualisatie__webmercatorquad?f=html)
- JSON: [https://api.pdok.nl/lv/bag/ogc/v1/styles/bag_standaardvisualisatie__webmercatorquad?f=json](https://api.pdok.nl/lv/bag/ogc/v1/styles/bag_standaardvisualisatie__webmercatorquad?f=json)

## 4. Legenda en statussen van de Panden in de BAG
In de HTML weergave zie je verschillende stijlen voor de statussen van de Panden in de BAG. Kijk goed naar de JSON-weergave en vergelijk de representatie van deze stijlen.
- Het is belangrijk om deze details goed door te nemen, omdat we later zelf stijlen gaan beheren en toepassen.

# Oefening 2: Het openen van de BAG vector tiles in QGIS

In deze oefening gaan we de BAG vector tiles in QGIS openen, eerst zonder styling en vervolgens met de styling van PDOK.

## Stappen om de BAG vector tiles in QGIS te openen zonder styling:
1. Open QGIS.
2. Ga naar het menu **Layer** (Laag) en kies voor **Add Layer** (Laag toevoegen).
3. Selecteer **Add Vector Layer** (Voeg Vectorlaag toe).
4. In het **Source** veld, voer de URL in voor de BAG vector tiles zonder styling:
   - [https://api.pdok.nl/lv/bag/ogc/v1/tiles/{z}/{x}/{y}.pbf](https://api.pdok.nl/lv/bag/ogc/v1/tiles/{z}/{x}/{y}.pbf)
5. Klik op **Add** (Toevoegen) om de vector tiles zonder styling in te laden.

## Stappen om de BAG vector tiles in QGIS te openen met de styling van PDOK:
1. Voeg de BAG vector tiles toe zoals hierboven beschreven.
2. Ga naar het **Layer Styling** venster in QGIS en voeg de URL voor de styling toe:
   - [https://api.pdok.nl/lv/bag/ogc/v1/styles/bag_standaardvisualisatie__webmercatorquad?f=json](https://api.pdok.nl/lv/bag/ogc/v1/styles/bag_standaardvisualisatie__webmercatorquad?f=json)
3. Het is mogelijk dat je een waarschuwing ontvangt over een ontbrekend lettertype. Dit gaan we later oplossen.
4. De styling zal automatisch worden toegepast en de BAG tiles zullen nu correct gestyled worden weergegeven.

## Wat valt op wanneer de tiles zonder styling worden ingeladen?
- Zorg ervoor dat je voldoende inzoomt en let op de zoomniveaus.
- **Antwoord**: Zonder styling is er een groot vlak over alle objecten heen, namelijk de "woonplaats". Wanneer de styling wordt ingeladen, wordt dit vlak aangepast zodat de panden zichtbaar worden, en het vlak wordt naar de achtergrond verplaatst.

## Probleem met het lettertype:
- Bij het inladen van de styling kan een waarschuwing verschijnen dat het lettertype niet gevonden kan worden. 
- Open de **JSON** van de BAG en zoek naar het lettertype dat wordt genoemd.
  - Het lettertype is waarschijnlijk een Windows-specifiek lettertype. 
- **Oplossing**: Download en installeer het lettertype op je Windows-systeem. Hierdoor wordt het lettertype herkend en de labels zullen correct worden weergegeven.
- Gelukkig zijn er in de JSON meerdere lettertypen gedefinieerd als fallback, zodat de labels altijd zichtbaar zijn.

## Laad ook de vector tiles en de styling van de BRT in:
1. Voeg de BRT vector tiles toe op dezelfde manier:
   - [https://api.pdok.nl/brt/top10nl/ogc/v1/tiles/{z}/{x}/{y}.pbf](https://api.pdok.nl/brt/top10nl/ogc/v1/tiles/{z}/{x}/{y}.pbf)
2. Voeg de bijbehorende styling toe:
   - [https://api.pdok.nl/brt/top10nl/ogc/v1/styles/brt_standaardvisualisatie__webmercatorquad?f=json](https://api.pdok.nl/brt/top10nl/ogc/v1/styles/brt_standaardvisualisatie__webmercatorquad?f=json)

## Vraag:
- Hoeveel tijd denk je dat het zou kosten om de uitgebreide styling voor TOP10NL zelf in QGIS te configureren?
- **Antwoord**: Dit laat zien hoe het gebruik van de gestandaardiseerde styles via PDOK veel tijdwinst kan opleveren, aangezien de styling al is voorbereid en geen handmatige configuratie verei

# Oefening 3: Zelf de Styles Aanpassen

In deze oefening gaan we de stijlen van de vector tiles zelf aanpassen door de JSON handmatig te bewerken. Dit geeft je volledige controle over de stijl en helpt je te begrijpen hoe het technisch werkt.

## Stappen om de BGT vector tiles zonder stijlen in QGIS in te laden:
1. Open QGIS.
2. Voeg de BGT vector tiles toe zonder styling door de volgende URL in te voeren voor de vector tiles:
   - [https://api.pdok.nl/lv/bgt/ogc/v1/tiles/{z}/{x}/{y}.pbf](https://api.pdok.nl/lv/bgt/ogc/v1/tiles/{z}/{x}/{y}.pbf)
3. Laad de vector tiles laag in.

## Download de BGT Standaardvisualisatie in Mapbox formaat:
1. Download de JSON van de BGT Standaardvisualisatie via de PDOK API:
   - [https://api.pdok.nl/lv/bgt/ogc/v1/styles/bgt_standaardvisualisatie__webmercatorquad/metadata](https://api.pdok.nl/lv/bgt/ogc/v1/styles/bgt_standaardvisualisatie__webmercatorquad/metadata)
   - [https://api.pdok.nl/lv/bgt/ogc/v1/styles/bgt_standaardvisualisatie__webmercatornewquad?f=mapbox](https://api.pdok.nl/lv/bgt/ogc/v1/styles/bgt_standaardvisualisatie__webmercatornewquad?f=mapbox)
2. Let op de juiste projecties. Als je de WebMercator tiles gebruikt, gebruik dan ook de WebMercator stijlen.

## Laad de Stijl in QGIS:
1. Open de **Laageigenschappen** van de BGT vector tiles laag in QGIS.
2. Klik op **Stijl** en kies **Stijl laden**.
3. Kies de gedownloade JSON file voor de BGT Standaardvisualisatie en laad deze in.

## Uitleg over de JSON:
- De JSON die je hebt geladen, wordt via de webservice van PDOK ingeladen en bevat de stijlinstellingen voor de vector tiles.
- We gaan nu een kleur aanpassen, bijvoorbeeld de kleur van het water.

## Pas de kleur aan in de JSON:
1. Maak een kopie van het originele JSON bestand met een andere herkenbare naam.
2. Open dit nieuwe JSON bestand in een teksteditor (bijvoorbeeld Notepad of Visual Studio Code).
3. Zoek naar de stijl voor de waterloop. Een voorbeeld van de JSON voor de waterloop is:

   ```json
   {
       "filter": [
           "all",
           [
               "==",
               "type",
               "waterloop"
           ],
           [
               "==",
               "relatieve_hoogteligging",
               0
           ],
           [
               "==",
               "status",
               "bestaand"
           ]
       ],
       "id": "Waterloop waterdeel fill0",
       "type": "fill",
       "paint": {
           "fill-color": "#ff0000",
           "fill-outline-color": "#73e9ff",
           "fill-opacity": 0.5
       },
       "source": "bgt",
       "source-layer": "waterdeel"
   }

```
