const express = require('express')
const app = express()
const cors = require('cors');
const port = 8080

var amstelveen = require('./amstelveen')

app.use(cors(
    {
        origin: 'http://127.0.0.1:5500', // Only allow requests from this origin
        methods: 'GET,HEAD,PUT,PATCH,POST,DELETE', // Allow these HTTP methods
        credentials: true, // Allow cookies to be sent
      }
)); // Enable CORS for all routes

app.use('/demoservice/v1', amstelveen)


app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))