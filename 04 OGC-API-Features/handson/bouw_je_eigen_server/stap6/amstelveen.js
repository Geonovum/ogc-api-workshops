var express = require('express')
var router = express.Router()
var url = require('url');
var make = require('./landingPage');

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

  res.send('api description in html')

})

// define the about route
router.get('/collections/:collectionId', function (req, res) {
  res.send('collections/:collectionId')
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
