# Stap 5: Landing Page en Conformance invullen

In deze oefening gaan we de Landing page en Conformance invullen.
We gaan dit 'hardcoded'doen, zonder gebruik te maken van javascript modules, zodat we goed zien wat we maken (later kunnen we dit verder abstraheren). Alle antwoorden zijn in JSON.


## Stap 1:
Zoals altijd, ga naar de stap5 directory in de terminal, en installeer express als het de eerste keer is dat je node gaat opstarten in deze directory. `npm update`

## Code:

```javascript
...
var make = require('./landingPage');
...
router.get('/', function (req, res) {

  var landingPage = make.header("amstelveen", "Access to data about buildings in the city of amstelveen via a Web API that conforms to the OGC API Features specification.");
  landingPage.links.push(make.item("http://localhost:8080/demoservice/v1",             "self",         "application/json", "this document"));
  landingPage.links.push(make.item("http://localhost:8080/demoservice/v1/api",         "service-desc", "application/vnd.oai.openapi+json;version=3.0", "the API definition"));
  landingPage.links.push(make.item("http://localhost:8080/demoservice/v1/api.html",    "service-doc",  "text/html",        "the API documentation"));
  landingPage.links.push(make.item("http://localhost:8080/demoservice/v1/conformance", "conformance",  "application/json", "OGC API conformance classes implemented by this server"));
  landingPage.links.push(make.item("http://localhost:8080/demoservice/v1/collections", "data",         "application/json", "Information about the feature collections"));

  res.json(landingPage)
})

// The server SHALL support the HTTP GET operation at the path /conformance.
router.get('/conformance', function (req, res) {
  var conformance = {};
  conformance.conformsTo = [];
  conformance.conformsTo.push("http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/core");
  conformance.conformsTo.push("http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/oas30");
  conformance.conformsTo.push("http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/html");
  conformance.conformsTo.push("http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/geojson");
  res.json(conformance)
})

// The URIs of all API definitions referenced from the landing page SHALL support the HTTP GET method.
//
// A GET request to the URI of an API definition linked from the landing page (link relations
// service-desc or service-doc) with an Accept header with the value of the link property 
// type SHALL return a document consistent with the requested media type.
//
router.get('/api', function (req, res) {
  res.json('{api def document here}')
})

// 
router.get('/api.html', function (req, res) {
  res.send('api description in html')
})

```

## Test

Start node op:

```
node index.js
```

`Example app listening at http://localhost:8080`

In je browser of via Bruno

Landing Page:
http://localhost:8080/demoservice/v1

Resultaat:

> `{"title":"amstelveen","description":"Access to data about buildings in the city of amstelveen via a Web API that conforms to the OGC API Features specification.","links":[{"href":"http://localhost:8080/demoservice/v1","rel":"self","type":"application/json","title":"this document"},{"href":"http://localhost:8080/demoservice/v1/api","rel":"service-desc","type":"application/vnd.oai.openapi+json;version=3.0","title":"the API definition"},{"href":"http://localhost:8080/demoservice/v1/api.html","rel":"service-doc","type":"text/html","title":"the API documentation"},{"href":"http://localhost:8080/demoservice/v1/conformance","rel":"conformance","type":"application/json","title":"OGC API conformance classes implemented by this server"},{"href":"http://localhost:8080/demoservice/v1/collections","rel":"data","type":"application/json","title":"Information about the feature collections"}]}`

Best leesbaar voor een computer, iets minder voor een mens...

Conformance:
http://localhost8080/demoservice/v1/conformance

> `{"conformsTo":["http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/core","http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/oas30","http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/html","http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/geojson"]}`

Hetzelfde voor Conformanece, best leesbaar voor een computer, iets minder voor een mens. Maar dat hoeft ook niet, de Conformance references zijn enkel voor de computer bedoeld.

In stap 6 gaan we de Landing Page responses ook voor de mens leesbaar maken!

## Merk op
/api en /api.html zijn toegevoegd, maar hoeft niet volgens de spec. Beide documenten kunnen ook elders 'leven'

## Klaar voor de volgende stap
Klaar voor [Stap6](./../stap6/readme.md)!