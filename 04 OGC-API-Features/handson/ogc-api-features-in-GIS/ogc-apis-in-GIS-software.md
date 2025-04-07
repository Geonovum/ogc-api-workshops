# OGC API’s in GIS software

Voor deze opdrachten is GIS-software zoals QGIS vereist, die Open API Features kan verwerken.

*Tip: Als je QGIS gebruikt, installeer dan de PDOK Service Plugin via Plug-ins » Plug-ins beheren en installeren, en zoek naar PDOK. Voeg indien nodig ook de PDOK Locatieserver plugin toe.*

De voorbeelden die we laten zien zijn in de omgeving van Gouda, specifiek in de nieuwe woonwijk WesterGouwe, met RD-coördinaten: 106860, 446100. Je kunt dit gebied gebruiken, maar het is ook interessant om een eigen bekend gebied te kiezen waarvan je weet dat er recent terreinwijzigingen hebben plaatsgevonden.

## BGT API Features in QGIS

In deze oefening gaan we aan de slag met het laden van BGT API Features in QGIS.
Volg de onderstaande stappen om deze features toe te voegen aan je kaart en om
verschillende handelingen uit te voeren, zoals het opvragen van attributen en
het filteren van gegevens.

### Toevoegen van BGT API Features

1\. Ga in QGIS naar het paneel Browser en selecteer WFS/OGC API Features.

2\. Klik op Nieuwe verbinding toevoegen...

3\. Voer als URL in: https://api.pdok.nl/lv/bgt/ogc/v1/.

4\. Open de volgende feature collecties:

\- Wegdeel

\- OndersteunendWegdeel

\- BegroeidTerreindeel

\- OnbegroeidTerreindeel

\- Waterdeel

\- OndersteunendWaterdeel

\- Pand

\- OverigBouwwerk

5\. Geef de lagen eventueel een andere kleur door rechts te klikken op de
kaartlaag in het paneel Lagen en vervolgens Eigenschappen » Symbologie te
selecteren.

### Opvragen van Attributen

1\. Vergelijkbaar met het opvragen van attribuutgegevens van vector tiles, kun je
in QGIS attribuutgegevens opvragen van features met CTRL+SHIFT+I of de
ObjectIdentificatie-knop. Probeer dit voor een aantal objecten.

### Filteren op Attributen

1\. Dupliceer een laag, bijvoorbeeld de laag met BegroeidTerreindeel of Wegdeel.

2\. Klik met de rechtermuisknop op de gedupliceerde laag en kies Filteren.

3\. Gebruik de Querybouwer om te filteren op specifieke attribuutwaarden.
Bijvoorbeeld, filter de begroeide terreindelen op fysiek-voorkomen
'groenvoorziening' om alle gemeenteplantsoenen in het gebied te selecteren.

4\. Vul de volgende filter-expressie in: "fysiek_voorkomen" = 'groenvoorziening'
en klik op Test en daarna op OK.

![Afbeelding met tekst, schermopname, scherm, software Automatisch gegenereerde
beschrijving](media/3eaa7663ac6493f33e04361f5161819b.png)

### Filteren op Peildatum

1\. Om de situatie op 1 januari 2020 te bekijken, gebruik je hetzelfde mechanisme
als bij het filteren op attributen, maar nu op het datumtijd-attribuut
creation_date.

2\. Vul de volgende filter-expressie in: "creation_date" =
'2020-01-01T00:00:00.001Z' om de situatie op 1 januari 2020 te zien.

3\. Haal de situaties terug van verschillende peildata, bijvoorbeeld 1 januari
2018, 1 januari 2020 en 1 januari 2022.
