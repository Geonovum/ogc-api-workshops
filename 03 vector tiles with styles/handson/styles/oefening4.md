# Oefening 4: Labels toevoegen aan de vector tiles

**Doel**: Voeg labels toe aan de vector tiles door de bronhoudercodes van de
waterlopen weer te geven en leer hoe je objecten filtert op basis van
bronhouderinformatie.

1.  **Maak een kopie van het vorige JSON-bestand**  
    Maak een kopie van het eerder aangepaste JSON-bestand (met de kleur van
    waterlopen gewijzigd), en sla het op onder een andere naam.

2.  **Voeg de stijl voor de bronhoudercode toe**  
    Voeg de volgende JSON toe na de stijl met id **Waterloop waterdeel fill0**,
    direct na het stukje:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"source": "bgt",
"source-layer": "waterdeel"
},
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Voeg het volgende JSON-blok toe:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
    "id": "Waterdeel bronhoudercode",
    "type": "symbol",
    "paint": {
        "text-opacity": 1,
        "text-color": "#000000",
        "text-halo-color": "#ffffff",
        "text-halo-width": 1
    },
    "layout": {
        "text-field": "{bronhouder}",
        "text-font": [
            "system-ui",
            "-apple-system",
            "Segoe UI",
            "Roboto",
            "Helvetica Neue",
            "Arial",
            "Noto Sans",
            "Liberation Sans",
            "sans-serif",
            "Apple Color Emoji",
            "Segoe UI Emoji",
            "Segoe UI Symbol",
            "Noto Color Emoji"
        ],
        "text-size": 13,
        "text-rotate": 0
    },
    "source": "bgt",
    "source-layer": "waterdeel"
}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  **Begrijp de stijlconfiguratie**  
    Dit JSON-blok zorgt ervoor dat de **bronhoudercode** van de waterlopen wordt
    weergegeven als een label.

    -   Het **text-field** veld geeft aan welk attribuut van de waterlopen als
        label moet worden weergegeven, in dit geval {bronhouder}, dat de
        bronhoudercode bevat.

    -   De **paint** sectie bepaalt de visuele eigenschappen van het label,
        zoals de kleur (text-color), de halo (de schaduw van het label), en de
        opaciteit (text-opacity).

    -   De **layout** sectie bepaalt de opmaak van het label, zoals het
        lettertype en de grootte van de tekst (text-size).

Kies een lettertype naar voorkeur uit de lijst in **text-font**, of voeg je
eigen lettertype toe.

1.  **Sla het JSON-bestand op en laad het in QGIS**  
    Sla de gewijzigde JSON op en laad deze in QGIS via de **Laageigenschappen**
    van de BGT vector tiles laag. De bronhoudercodes zouden nu als labels
    zichtbaar moeten zijn op de kaart.

2.  **Filteren van objecten op bronhoudercode**  
    Als je alleen objecten van bepaalde bronhouders wilt weergeven, kun je het
    **filter** veld aanpassen. Bijvoorbeeld, om geen labels weer te geven voor
    objecten van bronhouder **gemeente Zuidplas**, voeg je de volgende
    filterregel toe:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"filter": [
    "!=",
    "bronhouder",
    "G1892"
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dit zorgt ervoor dat objecten met bronhoudercode **G1892** (gemeente Zuidplas)
geen labels krijgen.

**Tip: Maak onderscheid tussen eigen en andere BGT-objecten**  
Om visueel onderscheid te maken tussen objecten van je eigen bronhoudercode en
objecten van andere bronhouders, kun je twee aparte stijlen maken.

1.  **Voor je eigen objecten**: Stel een stijl in met een filter dat alleen de
    objecten van jouw bronhoudercode toont. Dit doe je door de bronhoudercode in
    de filter te specificeren.

2.  **Voor de objecten van andere bronhouders**: Maak een tweede stijl waarin je
    een filter toevoegt om objecten van andere bronhouders te selecteren. Pas in
    deze stijl bijvoorbeeld de opaciteit (fill-opacity of text-opacity) aan,
    zodat deze objecten minder opvallen.

Daarnaast kun je in deze stijl de **bronhoudercode** van de niet-eigen objecten
als label tonen. Dit kan handig zijn om visueel aan te geven van welke
bronhouder de objecten afkomstig zijn.

Dit helpt om visueel onderscheid te maken tussen de objecten die je zelf beheert
en die van een andere bronhouder, en toont tevens de bronhoudercode van de
andere objecten, zodat je snel kunt zien welke bronhouder ze vertegenwoordigen.
