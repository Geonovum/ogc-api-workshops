var express = require('express')
var router = express.Router()

// The server SHALL support the HTTP GET operation at the path /.
router.get('/', function (req, res) {
  res.send('amstelveen landing page')
})

// The server SHALL support the HTTP GET operation at the path /conformance.
router.get('/conformance', function (req, res) {
  res.send('conformance page')
})

// Collections provides information about and access to the collections.
// The server SHALL support the HTTP GET operation at the path /collections.
router.get('/collections', function (req, res) {
  res.send('collections on this server')
})

// The server SHALL support the HTTP GET operation at the path
router.get('/collections/:collectionId', function (req, res) {
  console.log(req.params);
  res.send('collections on this server met bomen')
})

// define the about route
router.get('/collections/:collectionId/items', function (req, res) {
  res.send('collections on this server met bomen items')
})

// define the about route
router.get('/collections/:collectionId/items/:item', function (req, res) {
  console.log(req.params);
  res.send('collections on this server met bomen items id')
})

module.exports = router
