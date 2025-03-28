const express = require('express')
const app = express()
const port = 8080

app.get('/', (req, res) => 
    res.send('Hello World, step 2!'))

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))
