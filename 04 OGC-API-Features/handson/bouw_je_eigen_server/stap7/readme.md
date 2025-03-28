# Stap 7:  Wat heeft amstelveen te bieden qua geo bestanden?

(Met dank aan Michel Stuyts, (voormalig) GIS-coördinator. Zie ook op https://michelstuyts.be/ - https://stuyts.xyz)

## Stap 1:
Zoals altijd, ga naar de stap7 directory in de terminal, en installeer express als het de eerste keer is dat je node gaat opstarten in deze directory. `npm update`

## Lezen van de Datasets

in `amstelveen.js` voegen we een stukje code toe om geojson bestanden uit de data folder te lezen:

```javascript
var path = require('path');
var fs = require('fs');

var files = fs.readdirSync(path.join(__dirname, "data")).filter(fn => fn.endsWith('.geojson'));
for (i = 0; i < files.length; i++)
  files[i] = files[i].replace(/\.[^/.]+$/, "");
```

## Code voor `/collections`

De `/collections` route breiden we uit met een functie die de geojson files representeert.

Ook hier ondersteunen we de menselijk leesbare versie in HTML (met collections.template) en de machine leesbare versie in JSON.

```javascript

...
// define the about route
router.get('/collections', function (req, res) {

  var urlParts = url.parse(req.url, true);
  if (null == urlParts.query.f) {
    res.send(make.collections("html", files));
  }
  else if ("json" == urlParts.query.f) {
    res.json(make.collections("json", files));
  }
  else if ("html" == urlParts.query.f)
    res.send(make.collections("html", files));
  else
    res.json(400, "{'code': 'InvalidParameterValue', 'description': 'Invalid format'}")

})

...

```

## Testen:
Run de app

`Example app listening at http://localhost:8080`

In je browser of via Bruno

Landing Page:
- http://localhost:8080/demoservice/v1/collections
- http://localhost:8080/demoservice/v1/collections?f=json
- http://localhost:8080/demoservice/v1/collections?f=html

Resultaat:

in JSON
```json
{
  "links": [
    {
      "href": "http://localhost:8080/demoservice/v1/collections",
      "rel": "self",
      "type": "application/json",
      "title": "Metadata about the feature collections"
    }
  ],
  "collections": [
    {
      "title": "buurten",
      "description": "buurten",
      "links": [
        {
          "href": "http://localhost:8080/demoservice/v1/collections/buurten/items",
          "rel": "item",
          "type": "application/json",
          "title": "buurten"
        }
      ]
    },
    {
      "title": "energielabels",
      "description": "energielabels",
      "links": [
        {
          "href": "http://localhost:8080/demoservice/v1/collections/energielabels/items",
          "rel": "item",
          "type": "application/json",
          "title": "energielabels"
        }
      ]
    },
    {
      "title": "gemeenteGrens",
      "description": "gemeenteGrens",
      "links": [
        {
          "href": "http://localhost:8080/demoservice/v1/collections/gemeenteGrens/items",
          "rel": "item",
          "type": "application/json",
          "title": "gemeenteGrens"
        }
      ]
    },
    {
      "title": "kamersgewijzeVerhuur",
      "description": "kamersgewijzeVerhuur",
      "links": [
        {
          "href": "http://localhost:8080/demoservice/v1/collections/kamersgewijzeVerhuur/items",
          "rel": "item",
          "type": "application/json",
          "title": "kamersgewijzeVerhuur"
        }
      ]
    },
    {
      "title": "NAPPeilmerken",
      "description": "NAPPeilmerken",
      "links": [
        {
          "href": "http://localhost:8080/demoservice/v1/collections/NAPPeilmerken/items",
          "rel": "item",
          "type": "application/json",
          "title": "NAPPeilmerken"
        }
      ]
    },
    {
      "title": "zonnepanelen",
      "description": "zonnepanelen",
      "links": [
        {
          "href": "http://localhost:8080/demoservice/v1/collections/zonnepanelen/items",
          "rel": "item",
          "type": "application/json",
          "title": "zonnepanelen"
        }
      ]
    }
  ]
}
```

in HTML:

> Collections in this service

Name | Description
------ | -------------
[buurten](http://localhost:8080/demoservice/v1/collections/buurten)|buurten|
[energielabels](http://localhost:8080/demoservice/v1/collections/energielabels)|energielabels|
[gemeenteGrens](http://localhost:8080/demoservice/v1/collections/gemeenteGrens)|gemeenteGrens|
[kamersgewijzeVerhuur](http://localhost:8080/demoservice/v1/collections/kamersgewijzeVerhuur)|kamersgewijzeVerhuur|
[NAPPeilmerken](http://localhost:8080/demoservice/v1/collections/NAPPeilmerken)|NAPPeilmerken|
[zonnepanelen](http://localhost:8080/demoservice/v1/collections/zonnepanelen)|zonnepanelen|


## Klaar voor de volgende stap
Klaar voor [Stap8](./../stap8/readme.md)!
