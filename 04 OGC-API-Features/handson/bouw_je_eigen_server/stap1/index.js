var http = require('http');
var port = 8080

console.log(`Creating server http://localhost:${port}`)

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello World!');
}).listen(port); 
