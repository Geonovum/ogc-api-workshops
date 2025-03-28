# Howto: Openen OGC API Features Tiles in QGIS

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

---

NB.
De PDOK OGC API Features van bv de BAG of BGT bevatten standaard historie.
Deze API's kun je het beste bevragen met een datetime parameter om alleen de 'huidige' features op te halen.
bv: 
```
https://api.pdok.nl/lv/bgt/ogc/v1?datetime=2025-04-01T00:00:00.000Z
```