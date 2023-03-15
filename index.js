const express = require('express')
const sqlite3 = require('sqlite3').verbose();
const cors = require('cors');

const app = express()
const port = process.env.PORT || 3000;

app.use(express.json({expended: true}))
app.use(cors());

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})

app.get('/videos', (req, res) => {
  let db = new sqlite3.Database('mathapp.db');

  db.all('SELECT * FROM videos', [], (err, rows) => {
    if (err) {
      throw err;
    }
    res.send(rows)
  });

  db.close();
});

app.post('/videos', (req, res) => {
  const db = new sqlite3.Database('mathapp.db');
  
  db.run(`INSERT INTO videos (author, title, url) VALUES ("${req.body.author}", "${req.body.title}", "${req.body.url}");`, () => {
    res.send('done')
  });

  db.close();
});