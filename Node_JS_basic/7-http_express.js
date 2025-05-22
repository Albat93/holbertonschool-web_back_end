const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.set('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  try {
    const output = await countStudents(process.argv[2]);
    res.set('Content-Type', 'text/plain');
    res.send(`This is the list of our students\n${output}`);
  } catch (error) {
    res.set('Content-Type', 'text/plain');
    res.send(`This is the list of our students\n${error.message}`);
  }
});

// Démarrer le serveur
app.listen(port);

module.exports = app;
