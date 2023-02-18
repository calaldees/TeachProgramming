const express = require('express')
const app = express()
const port = 8000

// Init Express ----------------------------------------------------------------

app.use(express.json())
const cors = require('cors')
app.use(cors())

// Variables -------------------------------------------------------------------

const SCORES = []

// Routes ----------------------------------------------------------------------

app.get('/', (req, res) => {
    res.sendFile('client.html', {root: __dirname})
})

app.get('/score/', (req, res) => {
    res.json(["TODO",])
})

app.post('/score/', (req, res) => {
    res.status(201).json(req.body)
})

app.get('/word/', (req, res) => {
    res.status(200).json(["TODO",])
})


// Serve -----------------------------------------------------------------------

app.listen(port, () => {
    console.log(`Listening at http://localhost:${port}`)
})

/*
// https://expressjs.com/en/guide/error-handling.html
function logErrors (err, req, res, next) {
  console.error(err.stack)
  next(err)
}
app.use(logErrors)
app.use(function(req, res, next){
  console.log('no route', req.originalUrl);
  res.status(404).type('txt').send('Not found');
  next()
})
*/

// Docker container exit handler - https://github.com/nodejs/node/issues/4182
process.on('SIGINT', function() {process.exit()})
