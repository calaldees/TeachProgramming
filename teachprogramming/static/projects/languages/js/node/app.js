// https://nodejs.org/en/docs/guides/getting-started-guide/

const http = require('http');

const hostname = '0.0.0.0';  // had to change this from 127.0.0.1 to serve on all interfaces
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

// https://stackoverflow.com/a/53535316/3356840
process.on('SIGINT', function() {
  console.log( "\nGracefully shutting down from SIGINT (Ctrl-C)" );
  // some other closing procedures go here
  process.exit(0);
});