# Stap 2

Installatie van Express, het gaat ons leven makkelijker maken om om te gaan met paden in http
Op de website van [Express](https://expressjs.com) vind je alle information over paden in http. Je hoeft niet naar de Express website te gaan om het te installeren, we installeren Express via de node package manager `npm`

> Express is a minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications.


## Installer Express (via npm)

Ga naar de directory van stap2 (in de terminal tab), en typ:

```
npm update
```

Na de installatie zie je:

```
...
+ express@4.18.2
added 64 packages, and audited 65 packages in 2s

found 0 vulnerabilities
```

## Start NodeJS (met ExpressJS)

ExpressJS wordt verkort tot Express, net als NodeJS verkort wordt tot Node

Code:

```
const express = require('express')
const app = express()
const port = 8080

app.get('/', (req, res) => res.send('Hello World, step 2!'))

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))
```

Starten doe je op dezelfde manier als in `stap 1` , Driehoek met bug, dan groene driehoek met Launch Program of 'Run and Debug' (en evt NodeJS kiezen)

Op je scherm:
```
Example app listening at http://localhost:8080
```

Voor de geeks: [hoe werken callbacks](https://www.freecodecamp.org/news/nodejs-callbacks/)

## Testen in een browser:
http://localhost:8080

> `Hello World!`

Echter, elk ander pad werkt nu niet meer
http://localhost/joepie

geeft:
> `Cannot GET /joepie`

en dat is prima (voor het moment)

## Klaar voor de volgende stap
Klaar voor [Stap3](./../stap3/readme.md)!
