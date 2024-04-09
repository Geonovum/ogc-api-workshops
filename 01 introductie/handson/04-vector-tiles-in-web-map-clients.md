### Vector Tiles in Web Map Clients

In deze oefening gaan we dieper in op het gebruik van vector tiles van de BAG in MapLibre. Hieronder volgen de stappen om deze vector tiles toe te voegen aan een MapLibre-kaart en enkele interactieve functies toe te passen.

#### Stap 1: Initialiseer een lege MapLibre-kaart

Initialiseer een lege MapLibre-kaart en pas eventueel het centrale punt van de kaart aan naar een andere locatie.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>BAG Vector Tiles in MapLibre</title>
    <meta property="og:description" content="Add a vector source to a map." />
    <meta charset='utf-8'>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel='stylesheet' href='https://unpkg.com/maplibre-gl/dist/maplibre-gl.css' />
    <script src='https://unpkg.com/maplibre-gl/dist/maplibre-gl.js'></script>
    <style>
        body { margin: 0; padding: 0; }
        html, body, #map { height: 100%; }
    </style>
</head>
<body>
<div id="map"></div>
<script>
const map = new maplibregl.Map({
    container: 'map',			
    style: {version: 8,sources: {},layers: []},
    zoom: 17,
    center: [4.1626292, 51.901662] // Voeg hier jouw locatie toe
});

map.on('load', () => {
    // Voeg de vector tiles bronnen en lagen toe
});
</script>
</body>
</html>
```

#### Stap 2: Voeg de BAG Vector Tiles Panden toe als databron

Voeg de BAG Vector Tiles als databron toe aan het <script> element na het initialiseren van een nieuwe MapLibre-kaart. Kies de laag 'pand' om aan de kaart toe te voegen en pas indien nodig de kleur van de panden aan.

```javascript
 // Voeg de vector tiles bronnen en lagen toe
    map.addSource('bag', {
        type: 'vector',
        url: 'https://api.pdok.nl/lv/bag/ogc/v1_0/tiles/WebMercatorQuad?f=tilejson'
    });

    map.addLayer({
        'id': 'bag-pand',
        'type': 'fill',
        'source': 'bag',
        'source-layer': 'pand',
        'paint': {
            'fill-color': '#0080ff',
            'fill-opacity': 0.5
        }
    });

```

* Waarom liggen panden over elkaar heen wanneer je de default-center gebruikt?

#### Stap 3: Filter de gesloopte gebouwen uit de vector tiles features

Voeg de code toe om de gesloopte gebouwen uit de vector tiles features te filteren. Dit zorgt ervoor dat de gesloopte panden niet worden weergegeven op de kaart.
Let op: plaats de javascript binnen de map.on('load') functie.

```javascript
    // Filter gesloopte gebouwen
    map.setFilter('bag-pand', ['!=', 'status', 'Pand gesloopt']);
```

Wat gebeurt er wanneer je de code voor het filteren van gesloopte gebouwen toevoegt?

#### Stap 4: Tonen van gegevens van een feature in een popup

Voeg een click-event toe aan de kaart, zodat je de gegevens van het bovenste vector tile feature kunt bekijken in een popup wanneer erop wordt geklikt.
Let op: plaats de javascript binnen de map.on('load') functie.

```javascript
// Click event toevoegen
    map.on('click', function (e) {
        var features = map.queryRenderedFeatures(e.point); 
        if (features.length > 0) {
            console.log(features); 
            var popup = new maplibregl.Popup() 
                .setLngLat(e.lngLat)
                .setHTML('<h3>' + features[0].properties.id + '</h3><p>' + features[0].properties.bouwjaar + '</p>')
                .addTo(map); 
        }
    });
```

#### Stap 5: Kleur de BAG Panden op bouwjaar

Vervang de hexadecimale kleur in het script door een kleur-interpolatiefunctie op basis van het bouwjaar van de panden. Hierdoor worden de panden gekleurd op basis van hun bouwjaar.
Let op: plaats de javascript binnen de map.on('load') functie.

```javascript
// Kleur de BAG Panden op bouwjaar
    map.setPaintProperty('bag-pand', 'fill-color', [
        'interpolate',
        ['linear'],
        ['get', 'bouwjaar'], 
        1500, '#00ff00', 
        2025, '#0000ff'
    ]);
```
* Welke kleur krijgen de panden op basis van hun bouwjaar, volgens de kleur-interpolatiefunctie?


Je hebt nu een eigen interactieve BAG Vector Tiles Viewer met MapLibre gebouwd!
Bekijk het volledige script hier: 