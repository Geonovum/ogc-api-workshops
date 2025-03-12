# Oefening 5: Kleuren van de BAG-panden op basis van bouwjaar

In deze oefening gaan we de panden in de BAG (Basisregistratie Adressen en
Gebouwen) kleuren op basis van het bouwjaar. Omdat de interpolatie van kleuren
vanuit de JSON niet wordt ondersteund in QGIS, schakelen we over naar
**MapLibre** voor deze taak.

1.  **Open de MapLibre Maputnik interface**:

    -   Gebruik de volgende link om de MapLibre interface te openen:  
        [MapLibre
        Maputnik](https://maplibre.org/maputnik/?x=132000&y=455000&z=9.05&r=0&l=&layer=2368153705%7E0#17.25/52.339602/4.962838).

2.  **Download de JSON van de BAG standaardvisualisatie in WebMercator**:

    -   Download de JSON van de BAG standaardvisualisatie:  
        [BAG Standaardvisualisatie
        WebMercator](https://api.pdok.nl/lv/bag/ogc/v1/styles/bag_standaardvisualisatie__webmercatorquad?f=mapbox).

3.  **Open de JSON in een teksteditor**:

    -   Verwijder alle stijlen voor lagen behalve die van de panden. Je houdt de
        volgende stukken over in de JSON:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"layers": [
  {
    "id": "pand",
    "type": "fill",
    "paint": {
      "fill-opacity": 1,
      "fill-color": {
        "property": "status",
        "type": "categorical",
        "default": "transparent",
        "stops": [
          ["Bouwvergunning verleend", "rgb(105,213,156)"],
          ["Bouw gestart", "rgb(105,213,156)"],
          ["Pand in gebruik (niet ingemeten)", "rgb(146,146,146)"],
          ["Pand in gebruik", "rgb(146,146,146)"],
          ["Verbouwing pand", "rgb(81,156,156)"],
          ["Sloopvergunning verleend", "rgb(255,204,204)"],
          ["Pand buiten gebruik", "rgb(255,255,255)"],
          ["Pand geselecteerd", "rgb(195, 195, 205)"]
        ]
      }
    },
    "source": "bag",
    "source-layer": "pand"
  },
  {
    "id": "outline pand",
    "type": "line",
    "paint": {
      "line-color": {
        "property": "status",
        "type": "categorical",
        "default": "transparent",
        "stops": [
          ["Bouwvergunning verleend", "rgb(0,0,0)"],
          ["Bouw gestart", "rgb(0,0,0)"],
          ["Pand in gebruik (niet ingemeten)", "rgb(0,0,0)"],
          ["Pand in gebruik", "rgb(0,0,0)"],
          ["Verbouwing pand", "rgb(0,0,0)"],
          ["Sloopvergunning verleend", "rgb(0,0,0)"],
          ["Pand buiten gebruik", "rgb(0,0,0)"],
          ["Pand geselecteerd", "rgb(0,0,0)"]
        ]
      },
      "line-width": 0.5
    },
    "source": "bag",
    "source-layer": "pand"
  }
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  **Voeg een filter toe voor niet-gesloopte panden**:

    -   We willen alleen panden weergeven die niet de status 'Pand gesloopt'
        hebben. Voeg hiervoor het volgende filter toe aan beide lagen:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"filter": [
  "all",
  ["!=", "status", "Pand gesloopt"]
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  **Pas de kleur aan op basis van het bouwjaar**:

    -   De kleuren van de panden moeten gradueel veranderen op basis van het
        bouwjaar. We gebruiken een **interpolate** om de kleuren te variëren van
        1900 (groen) tot 2025 (blauw). Pas de fill-color van de panden en de
        line-color van de rand aan als volgt:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"paint": {
  "fill-opacity": 1,
  "fill-color": [
    "interpolate",          
    ["linear"],
    ["get", "bouwjaar"],
    1900, "#00ff00",  // Kleur voor bouwjaar 1900
    2025, "#0000ff"   // Kleur voor bouwjaar 2025
  ]
}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En voor de randkleur van de panden:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"paint": {
  "line-width": 1,
  "line-color": "#000000"  // Zwart voor de rand van de panden
}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  **Sla de JSON op en open in MapLibre Maputnik**:

    -   Sla de aangepaste JSON op en laad deze in MapLibre Maputnik via de optie
        **Open » Open local Style**.

![Afbeelding met tekst, schermopname, software, Multimediasoftware Door AI
gegenereerde inhoud is mogelijk
onjuist.](media/05b4986d701d65f26547c93e90d3b12b.png)

![Afbeelding met tekst, schermopname, Multimediasoftware, software Door AI
gegenereerde inhoud is mogelijk
onjuist.](media/ff4fa539be764871b3af58a1e8f0e705.png)
