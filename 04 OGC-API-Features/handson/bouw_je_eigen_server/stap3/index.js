const express = require('express')
const app = express()
const port = 8080

app.get('/', function (req, res) {
    res.send('Hello World, step3!')
  })

app.get('/about', function (req, res) {
    res.send('About!')
  })

app.post('/', function (req, res) {
    res.send('Got a POST request')
  })

app.put('/user', function (req, res) {
    res.send('Got a PUT request at /user')
  })

app.delete('/user', function (req, res) {
    res.send('Got a DELETE request at /user')
  })

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))
