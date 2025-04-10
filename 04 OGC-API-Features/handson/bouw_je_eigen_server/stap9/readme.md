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

`Example app listening at http://localhost:8080`

In je browser of via Bruno

Landing Page:
- http://localhost:8080/demoservice/v1/collections/buurten
- http://localhost:8080/demoservice/v1/collections/buurten/items?f=json
- http://localhost:8080/demoservice/v1/collections/buurten/items?f=html

Resultaat:

### in JSON
```json
{"type":"FeatureCollection","name":"Buurten","crs":{"type":"name","properties":{"name":"urn:ogc:def:crs:OGC:1.3:CRS84"}},"features":[{"type":"Feature","properties":{"fid":1,"buurtcode":"BU03620401","buurtnaam":"Stadshart","wijkcode":"WK036204","gemeentecode":"GM0362","gemeentenaam":"Amstelveen","wijknaam":"Stadshart","id_kv":1},"geometry":{"type":"Polygon","coordinates":[[[4.857296745844306,52.306325723050186],[4.857297004962856,52.30632563433261],[4.857297137434973,52.30632546865092],[4.85729883009887,52.30632332723977],[4.857298916960706,52.306323051702],[4.857298968760995,52.3063228883552],[4.857299067866605,52.30632256973061],[4.857307042467379,52.30629714378192],[4.857307101887812,52.306296956202104],[4.857309372892447,52.30629722073251],[4.857426599379163,52.306310912157485],[4.857427012283511,52.30631096074372],[4.857427446432116,52.30631094920655],[4.857617414234491,52.30630713614032],[4.85827660261133,52.30629317965907],[4.858311654780662,52.30629244660668],[4.85833721801667,52.30629190479967],[4.858460313501634,52.3062892644571],[4.858461023354793,52.306289248755895],[4.858461736129609,52.306289233966574],[4.858578917941784,52.306286738732226],[4.858663862085824,52.30628515899538],[4.858665638115089,52.30628512558767],[4.85870499990461,52.30628436583862],[4.858706994618284,52.30628431453298],[4.858708990883629,52.30628425604396],[4.858715413838341,52.30628406813593],[4.85891440970203,52.306279465544634],[4.858935942463183,52.30627890111209],[4.85895747016029,52.30627826924413],[4.858978991327078,52.30627756993426],[4.859000513315683,52.3062768014177],...
```

### in HTML:

__Data from collection "buurten"__

__Links.__

self = buurten (application/json)

__Features__

__JSON Output__

{"type":"FeatureCollection","name":"Buurten","crs":{"type":"name","properties":{"name":"urn:ogc:def:crs:OGC:1.3:CRS84"}},"features":[{"type":"Feature","properties":{"fid":1,"buurtcode":"BU03620401","buurtnaam":"Stadshart","wijkcode":"WK036204","gemeentecode":"GM0362","gemeentenaam":"Amstelveen","wijknaam":"Stadshart","id_kv":1},"geometry":{"type":"Polygon","coordinates":[[[4.857296745844306,52.306325723050186],[4.857297004962856,52.30632563433261],[4.857297137434973,52.30632546865092],[4.85729883009887,52.30632332723977],[4.857298916960706,52.306323051702],[4.857298968760995,52.3063228883552],[4.857299067866605,52.30632256973061],[4.857307042467379,52.30629714378192],[4.857307101887812,52.306296956202104],[4.857309372892447,52.30629722073251],[4.857426599379163,52.306310912157485],[4.857427012283511,52.30631096074372],[4.857427446432116,52.30631094920655],[4.857617414234491,52.30630713614032],[4.85827660261133,52.30629317965907],[4.858311654780662,52.30629244660668],[4.85833721801667,52.30629190479967],[4.858460313501634,52.3062892644571],[4.858461023354793,52.306289248755895],[4.858461736129609,52.306289233966574],[4.858578917941784,52.306286738732226],[4.858663862085824,52.30628515899538],[4.858665638115089,52.30628512558767],[4.85870499990461,52.30628436583862],[4.858706994618284,52.30628431453298],[4.858708990883629,52.30628425604396],[4.858715413838341,52.30628406813593],[4.85891440970203,52.306279465544634],[4.858935942463183,52.30627890111209],[4.85895747016029,52.30627826924413],[4.858978991327078,52.30627756993426],[4.859000513315683,52.3062768014177],[4.859022028741729,52.3062759681554],...


## Leaflet client en CORS

Voor de leaflet client demo is er nog een extra functie toegevoegd in de index.js: cors - 'Cross Origin Resource Sharing'

Deze functie zorgt ervoor dat de (nodeJS/express) server requests toestaat vanuit javascript in de browser en een response terug geeft.

In de configuratie staat:

```
origin: 'http://127.0.0.1:5500'
```
In VS Code kun je een extensie 'Live Server' installeren waarmee je html pagina's kunt serveren. Live server doet dat standaard op poort 5500. Dus dat is de poort die hier opgegeven wordt. Deze moet eventueel aangepast worden als er een andere poort gebruikt wordt.

