### OGC-API-Features in Leaflet

In deze oefening gaan we dieper in op het gebruik van OGC-API-Features m.b.v. Leaflet

Je hebt een tekst-editor nodig, bijvoorbeeld Kladblok, Notepad++ of VS Code. Je kunt het HTML-bestand lokaal opslaan en vervolgens openen in een browser bijvoorbeeld Google Chrome.

#### Stap 1: Initialiseer een lege Leaflet kaart

Initialiseer een lege Leaflet-kaart en pas eventueel het centrale punt van de kaart aan naar een andere locatie.

```html
<!DOCTYPE html>
<html>
<head>
	<title>BGT-bakken in Watergrasbuurt Gouda</title>
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A==" crossorigin=""/>
  <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" crossorigin=""></script>
	<style>
		html, body {
			height: 100%;
			margin: 0;
		}
    #map {
			width: 100%;
			height: 100%;
		}
  </style>
</head>
<body>

<div id='map'></div>

<script>
  var map = L.map('map').setView([52.031, 4.715], 17);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
      'Contains OS data &copy; Crown copyright and database right 2021.'
  }).addTo(map);
</script>

</body>
</html>
```

#### Stap 2: Voeg de BGT bakken toe als databron

Voeg de BAG Vector Tiles als databron toe aan het <script> element na het initialiseren van een nieuwe MapLibre-kaart. Kies de laag 'pand' om aan de kaart toe te voegen en pas indien nodig de kleur van de panden aan.
Let op: plaats de javascript binnen de map.on('load') functie.

```javascript
  (async () => {
    const BGTbak = await fetch('https://api.pdok.nl/lv/bgt/ogc/v1/collections/bak/items?f=json&bbox=4.710,52.028,4.720,52.035', {
        headers: {
        'Accept': 'application/geo+json'
      }
    }).then(response => response.json());

    L.geoJSON(BGTbak, {
      pointToLayer: function (feature, latlng) {
        return L.marker(latlng, 
    );
      },
//	         onEachFeature: onEachFeature
    }).addTo(map);
  })();

```

* Waarom liggen panden over elkaar heen wanneer je de default-center gebruikt?

#### Stap 3: Maak een Popup

Voeg de code toe om een popup te maken in je viewer.

```javascript
  	function onEachFeature(feature, layer) {
		var popupContent = "<a href='https://api.pdok.nl/lv/bgt/ogc/v1/collections/bak/items/" + feature.id + "' target='_blank'>" + feature.id + "</a>";
		if (feature.popupContent) {
			popupContent += feature.popupContent;
		}
		layer.bindPopup(popupContent);
	}

```

En haal de 2 '//' weg voor 'onEachFeature'.


Je hebt nu een eigen interactieve BGT OGC-API-Feature Viewer met Leaflet gebouwd!

Bekijk het volledige script hier: 
https://github.com/Geonovum/ogc-api-workshops/blob/main/04%20OGC-API-Features/handson/ogc-api-features-webclient/leaflet/bgtbak.html