# OGC API’s in GIS software

## Voor deze opdrachten is GIS-software zoals QGIS vereist, die Vector Tiles en Open API Features kan verwerken.

## *Tip: Als je QGIS gebruikt, installeer dan de PDOK Service Plugin via Plug-ins » Plug-ins beheren en installeren, en zoek naar PDOK. Voeg indien nodig ook de PDOK Locatieserver plugin toe.*

## De voorbeelden die we laten zien zijn in de omgeving van Gouda, specifiek in de nieuwe woonwijk WesterGouwe, met RD-coördinaten: 106860, 446100. Je kunt dit gebied gebruiken, maar het is ook interessant om een eigen bekend gebied te kiezen waarvan je weet dat er recent terreinwijzigingen hebben plaatsgevonden.

## Vector Tiles in QGIS

### BAG Vector Tiles Openen

1.  Open QGIS en navigeer naar het Browser-paneel. Zoek naar Vector Tiles en
    klik op 'Nieuwe algemene verbinding...'

    ![Afbeelding met tekst, schermopname, scherm, software Automatisch
    gegenereerde beschrijving](media/be1c52b06c83f03d6ad05783abf09097.png)

2\. Vul het onderstaande venster in met de naam 'BAG Vector Tiles' en de URL:
https://api.pdok.nl/lv/bag/ogc/v1_0/tiles/WebMercatorQuad/{z}/{y}/{x}?f=mvt

\- Welk maximaal zoomniveau moet worden ingesteld voor de verbinding?

*Hint: Kijk op https://api.pdok.nl/lv/bag/ogc/v1_0/tiles/WebMercatorQuad.*

3\. Klik op OK en voeg de laag toe aan het QGIS-project via dubbelklikken of
rechtsklikken » Laag aan project toevoegen…

4\. Zoom in op een locatie in Nederland (gebruik eventueel een andere PDOK
achtergrondlaag zoals een luchtfoto of de BRT achtergrondkaart). Zoom in tot
ongeveer 1:3100 om gegevens te bekijken.

5\. Je ziet nu een kaart die vergelijkbaar is met de onderstaande afbeelding.

![](media/97eacc1b7f3e2756239e54a1a35b78ca.png)

### Styling toevoegen

In het Browser-paneel, klik met de rechtermuisknop op de BAG Vector Tiles onder
Vector Tiles, en selecteer "Verbinding bewerken…".

\- Bekijk de beschikbare stijlen op: <https://api.pdok.nl/lv/bag/ogc/v1_0/styles>

![Afbeelding met tekening, diagram, ontwerp Automatisch gegenereerde
beschrijving](media/af682fbcccafa9cc9d006e379183b316.png)

### BGT Vector Tiles in QGIS

Herhaal de bovenstaande stappen met de BGT Vector Tiles:

\- URL:
[https://api.pdok.nl/lv/bgt/ogc/v1_0/tiles/WebMercatorQuad/{z}/{y}/{x}?f=mvt](https://api.pdok.nl/lv/bgt/ogc/v1_0/tiles/WebMercatorQuad/%7bz%7d/%7by%7d/%7bx%7d?f=mvt)

\- Experimenteer met de verschillende stijlen op:
<https://api.pdok.nl/lv/bgt/ogc/v1_0/styles>

*Hint: Let op het zoomniveau tijdens het verkennen.*

Bekijk en combineer de BAG met de BGT Vector Tiles.

![](media/97bcc20e5c95ac6554c368165006d3bc.png)

### Informatie opvragen

#### Informatie over een object opvragen

Klik in de werkbalk Attributen op de knop ‘Objecten identificeren’ of via de
sneltoetscombinatie CTRL+SHIFT+I.

![](media/6c697c7473395a10fac56c143f7c2fee.png)

[https://api.pdok.nl/lv/bgt/ogc/v1_0/tiles/WebMercatorQuad/{z}/{y}/{x}?f=mvt](https://api.pdok.nl/lv/bgt/ogc/v1_0/tiles/WebMercatorQuad/%7Bz%7D/%7By%7D/%7Bx%7D?f=mvt)

Vraag de gegevens van één of meer objecten.

### 

### 

### ![](media/97bcc20e5c95ac6554c368165006d3bc.png)

### 

### Onder de motorkap

Om inzicht te krijgen in hoe QGIS de API's onderliggend bevraagt, openen we de
debugopties.

1.  Ga naar Beeld \> Panelen \> Debugging/Ontwikkelingstools en klik op de rode
    knop 'Log opnemen'.

    ![Afbeelding met tekst, software, Computerpictogram, schermopname
    Automatisch gegenereerde
    beschrijving](media/e393cff7f53fb69964ba6cccccd7119f.png)

2.  Zoom in/uit of schakel een of meer lagen in/uit om de API's opnieuw te
    bevragen. In het debugvenster verschijnen nu meerdere GET-verzoeken.

    ![Afbeelding met tekst, schermopname, nummer, scherm Automatisch
    gegenereerde beschrijving](media/61e5c9c7fcd4cc8c8dde5798a22ae040.png)

3.  Klik met de rechtermuisknop op een GET-verzoek en selecteer 'URL openen'.
    Herhaal dit voor zowel de BAG- als de BGT-vector tiles.

## BGT API Features

We gaan nu de BGT API Features laden in QGIS

Ga in QGIS in het paneel Browser naar WFS/ OGC API Features en selecteer Nieuwe
verbinding toevoegen…

Voer als URL in: <https://api.pdok.nl/lv/bgt/ogc/v1_0-demo/>.

### Opvragen van attributen

### Filteren op attributen

### Filteren op peildatum

106860, 446100

"creation_date" = '2020-01-01T00:00:00.001Z'

# Gebruiken van OGC API in Web map clients

<https://maplibre.org/maplibre-gl-js/docs/examples/vector-source/>

Vraag een vector tegel op.

**https://api.pdok.nl/lv/bag/ogc/v1_0/tiles/NetherlandsRDNewQuad/5/10/15**

?f=mvt achter het request.

**https://api.pdok.nl/lv/bag/ogc/v1_0/tiles/WebMercatorQuad?f=json**

<https://api.pdok.nl/lv/bgt/ogc/v1_0/>

<https://api.pdok.nl/lv/bgt/ogc/v1_0/tiles/NetherlandsRDNewQuad/12/2048/2050?f=mvt>

Het configureren van een OGC API Features Service in QGIS vereist een paar
stappen. Hier is een algemeen overzicht van wat je moet doen:

1\. Open QGIS: Start QGIS op je computer.

2\. Voeg een nieuwe laag toe: Ga naar het paneel 'Browser' in QGIS en zoek naar
de optie om een nieuwe laag toe te voegen. Dit kan variëren afhankelijk van de
versie van QGIS die je gebruikt, maar je zou een optie moeten vinden om een 'OGC
API Features'-laag toe te voegen.

3\. Kies het type verbinding: Klik op de optie voor een nieuwe verbinding en
selecteer 'OGC API Features' (dit kan worden aangeduid als WFS3 in sommige
versies van QGIS).

4\. Voer de URL in: Voer de URL in van de OGC API Features Service die je wilt
gebruiken. Deze URL wordt meestal verstrekt door de aanbieder van de service.

5\. Authenticatie instellen (optioneel): Als de service authenticatie vereist,
zorg er dan voor dat je de juiste authenticatie-instellingen configureert, zoals
gebruikersnaam en wachtwoord.

6\. Klik op 'Verbinden': Nadat je de URL hebt ingevoerd en eventuele
authenticatie-instellingen hebt geconfigureerd, klik je op 'Verbinden' om
verbinding te maken met de service.

7\. Kies de laag: Als de verbinding succesvol is, zou je een lijst met
beschikbare lagen moeten zien. Kies de laag die je wilt toevoegen aan je kaart.

8\. Configureer aanvullende instellingen: Afhankelijk van de specifieke service
kunnen er aanvullende instellingen zijn die je kunt configureren, zoals
attributen om op te halen of filters die moeten worden toegepast. Deze
instellingen kunnen variëren afhankelijk van de OGC API Features-implementatie
die je gebruikt.

9\. Voeg de laag toe aan je kaart: Nadat je alle instellingen hebt
geconfigureerd, klik je op 'Toevoegen' of 'OK' om de laag toe te voegen aan je
kaart.

10\. Bekijk en analyseer de gegevens: Nu zou je de toegevoegde laag moeten kunnen
zien in de kaartweergave van QGIS. Je kunt vervolgens de gegevens bekijken,
analyseren en bewerken zoals je normaal zou doen met andere lagen in QGIS.

Om OGC Vector Tiles te openen in QGIS, volg je deze stappen:

1\. Open QGIS: Start QGIS op je computer.

2\. Voeg een nieuwe laag toe: Ga naar het paneel 'Browser' in QGIS en zoek naar
de optie om een nieuwe laag toe te voegen.

3\. Kies het type verbinding: Klik op de optie voor een nieuwe verbinding en
selecteer 'OGC API Vector Tiles'.

4\. Voer de URL in: Voer de URL in van de OGC Vector Tiles-service die je wilt
gebruiken. Deze URL wordt meestal verstrekt door de aanbieder van de service.

5\. \*\*Authenticatie instellen\*\* (optioneel):

Als de service authenticatie vereist, configureer dan de juiste
authenticatie-instellingen, zoals gebruikersnaam en wachtwoord.

6\. \*\*Klik op 'Verbinden'\*\*:

Nadat je de URL hebt ingevoerd en eventuele authenticatie-instellingen hebt
geconfigureerd, klik je op 'Verbinden' om verbinding te maken met de service.

7\. \*\*Kies de tegelset en stijl\*\*:

Als de verbinding succesvol is, zou je een lijst met beschikbare tegelsets en
stijlen moeten zien. Kies de tegelset en stijl die je wilt toevoegen aan je
kaart.

8\. \*\*Pas eventuele aanvullende instellingen toe\*\*:

Afhankelijk van de specifieke service kunnen er aanvullende instellingen zijn
die je kunt configureren, zoals attributen om op te halen of filters die moeten
worden toegepast. Deze instellingen kunnen variëren afhankelijk van de OGC
Vector Tiles-implementatie die je gebruikt.

9\. \*\*Voeg de laag toe aan je kaart\*\*:

Nadat je alle instellingen hebt geconfigureerd, klik je op 'Toevoegen' of 'OK'
om de laag toe te voegen aan je kaart.

10\. \*\*Bekijk en analyseer de gegevens\*\*:

Nu zou je de toegevoegde laag moeten kunnen zien in de kaartweergave van QGIS.
Je kunt vervolgens de gegevens bekijken, analyseren en bewerken zoals je normaal
zou doen met andere lagen in QGIS.

Dit zijn de stappen die je moet volgen om OGC Vector Tiles te openen en te
gebruiken in QGIS. De exacte stappen kunnen variëren afhankelijk van de versie
van QGIS die je gebruikt en de specifieke kenmerken van de Vector Tiles-service
waarmee je verbinding maakt.
