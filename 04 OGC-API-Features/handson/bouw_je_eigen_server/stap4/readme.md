# Stap 4

We gaan een OGC API Features service maken voor amstelveen! Joepie
Het is te zeggen, we gaan de stubs opzetten voor de OGC API Feature service en ze even in detail gaan bekijken.

## 1 Voorbereiding:
Eerst even Express installeren (om de repo zo klein mogelijk te houden, zit `express` er niet bij en moet je het installeren `npm update` bij de eerste keer dat je de code runt in de directory. Eenmaal het er staat, ben je OK)


## 2 Tweede voorzichtige stapjes

```javascript
const express = require('express')
const app = express()
const port = 80

var amstelveen = require('./amstelveen')

app.use('/amstelveen/v1', amstelveen)

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))
```

Vanuit `index.js` verwijzen we naar de paden in `amstelveen.js` - netter en handiger

```javascript
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
```

We hebben een Landing Page, Conformance en Collections opgezet - mooi!
Dit zijn 3 essentiele paden die **moeten** aanwezig zijn

Laten we eens in de spec kijken wat we hier mee aan moeten:
- [Landing Page](http://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_api_landing_page)
- [Conformance](https://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_declaration_of_conformance_classes)
- [Feature collections](https://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_collections_)
- [Feature collection](https://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_collection_)
- [Feature](http://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_items_)

## Testen

http://localhost:8080/demoservice/v1

> `amstelveen landing page`

Merk op dat we in `index.js` het basispad `/demoservice/v1` definieren, en dan in `amstelveen.js` de verschillende routes beschrijven waar een OGC API Features server aan moet voldoen.

## Klaar voor de volgende stap
Klaar voor [Stap5](./../stap5/readme.md)!
