# Stap 9: Wat heeft amstelveen te bieden qua geo bestanden? (Cont.)

(Met dank aan Michel Stuyts, GIS-coördinator. Zie ook op https://michelstuyts.be/ - https://stuyts.xyz)

## Stap 1:
Zoals altijd, ga naar de stap9 directory in de terminal, en installeer express als het de eerste keer is dat je node gaat opstarten in deze directory. `npm update`

## Code for `/collections/:collectionId/items`

Nu vullende we `items' aan met de benodigde informatie:

```javascript

...
// define the about route
router.get('/collections/:collectionId/items', function (req, res) {
  if (null == dataDict[req.params.collectionId])
  {
    res.status(404).send("The requested URL " + req.url + " was not found on this server");
    return;
  }

  var urlParts = url.parse(req.url, true);
  if (null == urlParts.query.f) 
    res.send(make.items("html", req.params.collectionId, dataDict[req.params.collectionId]));
  else if ("json" == urlParts.query.f) 
    res.json(make.items("json", req.params.collectionId, dataDict[req.params.collectionId]));
  else if ("html" == urlParts.query.f)
    res.send(make.items("html", req.params.collectionId, dataDict[req.params.collectionId]));
  else
    res.json(400, "{'code': 'InvalidParameterValue', 'description': 'Invalid format'}") 
})

...

```

## Testen:
```
node index.js
```

`Example app listening at http://localhost:80`

In je browser of via PostMan

Landing Page:
- http://localhost/amstelveen/collections/groendienst/items
- http://localhost/amstelveen/collections/groendienst/items?f=json
- http://localhost/amstelveen/collections/groendienst/items?f=html

Resultaat:

### in JSON
```json
"{\"type\":\"FeatureCollection\",\"crs\":{\"type\":\"name\",\"properties\":{\"name\":\"EPSG:4326\"}},\"features\":[{\"type\":\"Feature\",\"geometry\":{\"type\":\"Point\",\"coordinates\":[4.4783351318391,51.114442184776]},\"properties\":{\"categorie\":\"GroepsopvangBabysEnPeuters\",\"categorietxt\":\"Groepsopvang baby's en peuters\",\"id\":146885,\"naam\":\"De Drie Klavertjes\",\"via\":\"http://poi.api.geopunt.be/v1/core?id=146885\",\"adres\":\"Duffelsesteenweg 353, 2550 amstelveen\",\"x\":4.4783351318391,\"y\":51.114442184776}},{\"type\":\"Feature\",\"geometry\":{\"type\":\"Point\",\"coordinates\":[4.4510933670167,51.13755372405]},\"properties\":{\"categorie\":\"GroepsopvangBabysEnPeuters\",\"categorietxt\":\"Groepsopvang baby's en peuters\",\"id\":147697,\"naam\":\"'t Brugske\",\"via\":\"http://poi.api.geopunt.be/v1/core?id=147697\",\"adres\":\"Antwerpsesteenweg 62, 2550 amstelveen\",\"x\":4.4510933670167,\"y\":51.13755372405}},{\"type\":\"Feature\",\"geometry\":{\"type\":\"Point\",\"coordinates\":[4.453777476859,51.125258504412]},\"properties\":{\"categorie\":\"GroepsopvangBabysEnPeuters\",\"categorietxt\":\"Groepsopvang baby's en peuters\",\"id\":150227,\"naam\":\"Kidz-Planet\",\"via\":\"http://poi.api.geopunt.be/v1/core?id=150227\",\"adres\":\"Blauwesteenstraat 77, 2550 amstelveen\",\"x\":4.453777476859,\"y\":51.125258504412}},{\"type\":\"Feature\",\"geometry\":{\"type\":\"Point\",\"coordinates\":[4.4562966861328,51.106771379376]},\"properties\":{\"categorie\":\"GroepsopvangBabysEnPeuters\",\"categorietxt\":\"Groepsopvang baby's en peuters\",\"id\":157884,\"naam\":\"'t Wisterke\",\"via\":\"http://poi.api.geopunt.be/v1/core?id=157884\",\"adres\":\"Beekboshoek 42, 2550 amstelveen\",\"x\":4.4562966861328,\"y\":51.106771379376}},{\"type\":\"Feature\",\"geometry\":{\"type\":\"Point\",\"coordinates\":[4.4722055491099,51.133144121845]},\"properties\":{\"categorie\":\"GroepsopvangBabysEnPeuters\",\"categorietxt\":\"Groepsopvang baby's en peuters\",\"id\":201645,\"naam\":\"Kinderopvang Speel-goed BVBA\",\"via\":\"http://poi.api.geopunt.be/v1/core?id=201645\",\"adres\":\"Kauwlei 15, 2550 amstelveen\",\"x\":4.4722055491099,\"y\":51.133144121845}},{\"type\":\"Feature\",\"geometry\":{\"type\":\"Point\",\"coordinates\":[4.4463372070709,51.131894192936]},\"properties\":{\"categorie\":\"GroepsopvangBabysEnPeuters\",\"categorietxt\":\"Groepsopvang baby's en peuters\",\"id\":228940,\"naam\":\"'t Lachebekje BVBA\",\"via\":\"http://poi.api.geopunt.be/v1/core?id=228940\",\"adres\":\"Mechelsesteenweg 94, 2550 amstelveen\",\"x\":4.4463372070709,\"y\":51.131894192936}},{\"type\":\"Feature\",\"geometry\":{\"type\":\"Point\",\"coordinates\":[4.4462532805616,51.131683104149]},\"properties\":{\"categorie\":\"GroepsopvangBabysEnPeuters\",\"categorietxt\":\"Groepsopvang baby's en peuters\",\"id\":234070,\"naam\":\"'t Lachebekje BVBA\",\"via\":\"http://poi.api.geopunt.be/v1/core?id=234070\",\"adres\":\"Mechelsesteenweg 102, 2550 amstelveen\",\"x\":4.4462532805616,\"y\":51.131683104149}}]}"
```

### in HTML:

Data from collection "GroepsopvangBabysEnPeutersamstelveen"

Links.

self = GroepsopvangBabysEnPeutersamstelveen (application/json)

Features

JSON Output

{"type":"FeatureCollection","crs":{"type":"name","properties":{"name":"EPSG:4326"}},"features":[{"type":"Feature","geometry":{"type":"Point","coordinates":[4.4783351318391,51.114442184776]},"properties":{"categorie":"GroepsopvangBabysEnPeuters","categorietxt":"Groepsopvang baby's en peuters","id":146885,"naam":"De Drie Klavertjes","via":"http://poi.api.geopunt.be/v1/core?id=146885","adres":"Duffelsesteenweg 353, 2550 amstelveen","x":4.4783351318391,"y":51.114442184776}},{"type":"Feature","geometry":{"type":"Point","coordinates":[4.4510933670167,51.13755372405]},"properties":{"categorie":"GroepsopvangBabysEnPeuters","categorietxt":"Groepsopvang baby's en peuters","id":147697,"naam":"'t Brugske","via":"http://poi.api.geopunt.be/v1/core?id=147697","adres":"Antwerpsesteenweg 62, 2550 amstelveen","x":4.4510933670167,"y":51.13755372405}},{"type":"Feature","geometry":{"type":"Point","coordinates":[4.453777476859,51.125258504412]},"properties":{"categorie":"GroepsopvangBabysEnPeuters","categorietxt":"Groepsopvang baby's en peuters","id":150227,"naam":"Kidz-Planet","via":"http://poi.api.geopunt.be/v1/core?id=150227","adres":"Blauwesteenstraat 77, 2550 amstelveen","x":4.453777476859,"y":51.125258504412}},{"type":"Feature","geometry":{"type":"Point","coordinates":[4.4562966861328,51.106771379376]},"properties":{"categorie":"GroepsopvangBabysEnPeuters","categorietxt":"Groepsopvang baby's en peuters","id":157884,"naam":"'t Wisterke","via":"http://poi.api.geopunt.be/v1/core?id=157884","adres":"Beekboshoek 42, 2550 amstelveen","x":4.4562966861328,"y":51.106771379376}},{"type":"Feature","geometry":{"type":"Point","coordinates":[4.4722055491099,51.133144121845]},"properties":{"categorie":"GroepsopvangBabysEnPeuters","categorietxt":"Groepsopvang baby's en peuters","id":201645,"naam":"Kinderopvang Speel-goed BVBA","via":"http://poi.api.geopunt.be/v1/core?id=201645","adres":"Kauwlei 15, 2550 amstelveen","x":4.4722055491099,"y":51.133144121845}},{"type":"Feature","geometry":{"type":"Point","coordinates":[4.4463372070709,51.131894192936]},"properties":{"categorie":"GroepsopvangBabysEnPeuters","categorietxt":"Groepsopvang baby's en peuters","id":228940,"naam":"'t Lachebekje BVBA","via":"http://poi.api.geopunt.be/v1/core?id=228940","adres":"Mechelsesteenweg 94, 2550 amstelveen","x":4.4463372070709,"y":51.131894192936}},{"type":"Feature","geometry":{"type":"Point","coordinates":[4.4462532805616,51.131683104149]},"properties":{"categorie":"GroepsopvangBabysEnPeuters","categorietxt":"Groepsopvang baby's en peuters","id":234070,"naam":"'t Lachebekje BVBA","via":"http://poi.api.geopunt.be/v1/core?id=234070","adres":"Mechelsesteenweg 102, 2550 amstelveen","x":4.4462532805616,"y":51.131683104149}}]}


## NB

Voor de leaflet client demo is er nog een extra functie toegevoegd in de index.js: cors - 'Cross Origin Resource Sharing'

