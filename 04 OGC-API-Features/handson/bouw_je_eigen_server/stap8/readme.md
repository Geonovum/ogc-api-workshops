# Stap 8: Wat heeft amstelveen te bieden qua geo bestanden? (Cont.)



(Met dank aan Michel Stuyts, GIS-coördinator. Zie ook op https://michelstuyts.be/ - https://stuyts.xyz)

## Stap 1:
Zoals altijd, ga naar de stap8 directory in de terminal, en installeer express als het de eerste keer is dat je node gaat opstarten in deze directory. `npm update`

## Code for `/collections/:collectionId`

In stap 7 hebben we de informatie voor Collections opgebouwd. Nu gaan we collectionId pagina opbouwen met specifieke informatie voor de collectie:

```javascript

...
// define the about route
router.get('/collections/:collectionId', function (req, res) {

  if (!files.includes(req.params.collectionId))
  {
    res.status(404).send("The requested URL " + req.url + " was not found on this server");
    return;
  }

  var urlParts = url.parse(req.url, true);
  if (null == urlParts.query.f) 
    res.send(make.collection("html", req.params.collectionId));
  else if ("json" == urlParts.query.f) 
    res.json(make.collection("json", req.params.collectionId));
  else if ("html" == urlParts.query.f)
    res.send(make.collection("html", req.params.collectionId));
  else
    res.json(400, "{'code': 'InvalidParameterValue', 'description': 'Invalid format'}") 
})

...

```

## Testen:
```
node index.js
```

`Example app listening at http://localhost:8080`

In je browser of via Bruno

Landing Page:
- http://localhost:8080/demoservice/v1/collections/buurten
- http://localhost:8080/demoservice/v1/collections/buurten?f=json
- http://localhost:8080/demoservice/v1/collections/buurten?f=html

Resultaat:

### in JSON
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
    }
  ]
}
```

### in HTML:

Metadata about the feature collections
Collections.
buurten (buurten)
buurten

Links for the collection

item = [buurten](http://localhost:8080/demoservice/v1/collections/buurten/items) (application/json)

Links

self = [Metadata about the feature collections](http://localhost:8080/demoservice/v1/collections) (application/json)

JSON output

Get raw [JSON](http://localhost:8080/demoservice/v1/collections?f=json)

## Klaar voor de volgende stap
Klaar voor [Stap9](./../stap9/readme.md)!

