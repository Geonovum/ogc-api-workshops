var express = require('express')
var router = express.Router()
var make = require('./landingPage');

// define the home page route
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
  res.json('{api def here in json}')
})

// 
router.get('/api.html', function (req, res) {
  res.send('api description in html')
})

// define the about route
router.get('/collections', function (req, res) {
  res.send('collections')

})

// define the about route
router.get('/collections/:collectionId', function (req, res) {
  res.send('collections collectionId')
})

// define the about route
router.get('/collections/:collectionId/items', function (req, res) {
  res.send('collections/:collectionId/items')
})

// define the about route
router.get('/collections/:collectionId/items/:item', function (req, res) {
  console.log(req.params);
  res.send('collections/:collectionId/items/:item')
})

module.exports = router
