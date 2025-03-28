# Stap 6: Landing Page in JSON & HTML

De Landing Page in Stap 5 was enkel beschikbaar in JSON, in deze les maken we die ook beschikbaar in HTML

Dit is een belangrijke stap: de API die resultaten kan geven voor 
  
  a) een machine (JSON) of 
  
  b) een mens (HTML)!

## Stap 1:
Zoals altijd, ga naar de stap6 directory in de terminal, en installeer express als het de eerste keer is dat je node gaat opstarten in deze directory. `npm update`

We gaan pug templates gebruiken om de html landigPage te maken. 
(pug is toegevoegd aan `package.json`)

## Code voor `/` (Landing Page)

```javascript
...
var make = require('./landingPage');
...
// define the home page route
router.get('/', function (req, res) {
  
  var contentType = "";
  var accept = req.headers.accept;
  if ("application/json" == accept)
    contentType = "json";
  else if ("text/html" == accept)
    contentType = "html";

  var urlParts = url.parse(req.url, true);
  if (null != urlParts.query.f)
  {
    if ("json" == urlParts.query.f)
      contentType = "json";
    else if ("html" == urlParts.query.f)
      contentType = "html";
    else {
      res.json(400, "{'code': 'InvalidParameterValue', 'description': 'Invalid format'}");
      return;
    }
  }

  if (contentType == "")
    contentType = "html";

  if ("json" == contentType)
    res.json(make.landingPage(contentType))
  else if ("html" == contentType)
    res.send(make.landingPage(contentType))

})
```

De javascript module [landingPage](./landingPage.js) maakt het JSON of HTML antwoord.


## Testen:
Run de app

`Example app listening at http://localhost:8080`

In je browser of Bruno

Landing Page:
- http://localhost:8080/demoservice/v1?f=json

Resultaat:

> `{"title":"amstelveen OGC API Feature server","description":"Access to data in the city of amstelveen via a Web API that conforms to the OGC API Features specification.","links":[{"href":"http://localhost:8080/demoservice/v1","rel":"self","type":"application/json","title":"this document"},{"href":"http://localhost:8080/demoservice/v1api","rel":"service-desc","type":"application/vnd.oai.openapi+json;version=3.0","title":"the API definition"},{"href":"http://localhost:8080/demoservice/v1api.html","rel":"service-doc","type":"text/html","title":"the API documentation"},{"href":"http://localhost:8080/demoservice/v1conformance","rel":"conformance","type":"application/json","title":"OGC API conformance classes implemented by this server"},{"href":"http://localhost:8080/demoservice/v1collections","rel":"data","type":"application/json","title":"Information about the feature collections"}]}`

Landing Page:
http://localhost:8080/demoservice/v1?f=html

Resultaat: 

> De menselijk leesbare pagina in HTML

## Klaar voor de volgende stap
Klaar voor [Stap7](./../stap7/readme.md)!
