var express = require('express')
var router = express.Router()
var url = require('url');
var make = require('./make');
var path = require('path');
var fs = require('fs');

var files = fs.readdirSync(path.join(__dirname, "data")).filter(fn => fn.endsWith('.geojson'));
for (i = 0; i < files.length; i++)
  files[i] = files[i].replace(/\.[^/.]+$/, "");

// define the home page route
router.get('/', function (req, res) {

  var urlParts = url.parse(req.url, true);
  if (null == urlParts.query.f)
    res.send(make.landingPage("html"))
  else if ("json" == urlParts.query.f)
    res.json(make.landingPage(urlParts.query.f))
  else if ("html" == urlParts.query.f)
    res.send(make.landingPage(urlParts.query.f))
  else
    res.json(400, "{'code': 'InvalidParameterValue', 'description': 'Invalid format'}")
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

  var urlParts = url.parse(req.url, true);
  if (null == urlParts.query.f) 
    res.send(make.collections("html", files));
  else if ("json" == urlParts.query.f) 
    res.json(make.collections("json", files));
  else if ("html" == urlParts.query.f)
    res.send(make.collections("html", files));
  else
    res.json(400, "{'code': 'InvalidParameterValue', 'description': 'Invalid format'}")
})

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

// define the about route
router.get('/collections/:collectionId/items', function (req, res) {
  console.log(req.params);
  res.send('collections/:collectionId/items/:item')
})

// define the about route
router.get('/collections/:collectionId/items/:item', function (req, res) {
  console.log(req.params);
  res.send('collections/:collectionId/items/:item')
})

module.exports = router
