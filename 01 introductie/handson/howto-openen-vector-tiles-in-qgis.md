# Howto: Openen OGC Vector Tiles in QGIS

Om OGC Vector Tiles te openen in QGIS, volg je deze stappen:

1\. Open QGIS: Start QGIS op je computer.

2\. Voeg een nieuwe laag toe: Ga naar het paneel 'Browser' in QGIS en zoek naar
de optie om een nieuwe laag toe te voegen.

3\. Kies het type verbinding: Klik op de optie voor een nieuwe verbinding en
selecteer 'OGC API Vector Tiles'.

4\. Voer de URL in: Voer de URL in van de OGC Vector Tiles-service die je wilt
gebruiken. Deze URL wordt meestal verstrekt door de aanbieder van de service.
Bij PDOK heet het de "URL template" vb: "https://api.pdok.nl/lv/bag/ogc/v1/tiles/WebMercatorQuad/{z}/{y}/{x}?f=mvt"
De andere 2 TileMatrixSets(NetherlndsRDNewQuad en EuropeanETRS89_LAEAQuad) werken nog niet goed in QGIS.

5\. Stel het minimale en maximale zoomniveau in. Deze is te vinden onder landingpage/tileMatrixSets.
Voor TileMatrixSets https://api.pdok.nl/lv/bag/ogc/v1/tileMatrixSets/WebMercatorQuad kun je 17 invullen bij het maximum.

6\. Authenticatie instellen (optioneel):

Als de service authenticatie vereist, configureer dan de juiste
authenticatie-instellingen, zoals gebruikersnaam en wachtwoord.

7\. Klik op 'Verbinden':

Nadat je de URL hebt ingevoerd en eventuele authenticatie-instellingen hebt
geconfigureerd, klik je op 'Verbinden' om verbinding te maken met de service.

8\. Kies de tegelset en stijl:

Als de verbinding succesvol is, zou je een lijst met beschikbare tegelsets en
stijlen moeten zien. Kies de tegelset en stijl die je wilt toevoegen aan je
kaart.

9\. Pas eventuele aanvullende instellingen toe:

Afhankelijk van de specifieke service kunnen er aanvullende instellingen zijn
die je kunt configureren, zoals attributen om op te halen of filters die moeten
worden toegepast. Deze instellingen kunnen variëren afhankelijk van de OGC
Vector Tiles-implementatie die je gebruikt.

10\. Voeg de laag toe aan je kaart:

Nadat je alle instellingen hebt geconfigureerd, klik je op 'Toevoegen' of 'OK'
om de laag toe te voegen aan je kaart.

10\. Bekijk en analyseer de gegevens:

Zoom ergens in Nederland in naar schaal 1:3000. Als je te ver uitgezoomd bent zie je niets.

Nu zou je de toegevoegde laag moeten kunnen zien in de kaartweergave van QGIS.
Je kunt vervolgens de gegevens bekijken, analyseren en bewerken zoals je normaal
zou doen met andere lagen in QGIS.

Dit zijn de stappen die je moet volgen om OGC Vector Tiles te openen en te
gebruiken in QGIS. De exacte stappen kunnen variëren afhankelijk van de versie
van QGIS die je gebruikt en de specifieke kenmerken van de Vector Tiles-service
waarmee je verbinding maakt.
