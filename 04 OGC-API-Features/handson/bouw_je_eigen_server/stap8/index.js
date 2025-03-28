const express = require('express')
const app = express()
const port = 8080

var amstelveen = require('./amstelveen')

app.use('/demoservice/v1', amstelveen)


app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))