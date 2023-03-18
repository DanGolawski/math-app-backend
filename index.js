const express = require('express')
const sqlite3 = require('sqlite3').verbose();
const cors = require('cors');
const mathBooksModule = require('./math-books');
const additionalServicesModule = require('./additional-services');

const app = express()
const port = process.env.PORT || 3000;

app.use(express.json({expended: true}))
app.use(cors());

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})

// VIDEOS
app.post('/videos', (req, res) => {
  const db = new sqlite3.Database('mathapp.db');
  additionalServicesModule.addNewVideo(req.body, db).then(message => res.send(message));
  db.close();
});

app.get('/videos', async (req, res) => {
  let db = new sqlite3.Database('mathapp.db');
  const videos = await additionalServicesModule.getVideos(db);
  res.status(200).send(videos)
  db.close();
});

// RECOMMENDED BOOKS
app.post('/recommended-book', (req, res) => {
  const db = new sqlite3.Database('mathapp.db');
  additionalServicesModule.addNewRecommendedBook(req.body, db).then(message => res.status(200).send(message));
  db.close();
});

app.get('/recommended-books', (req, res) => {
  const db = new sqlite3.Database('mathapp.db');
  additionalServicesModule.getRecommendedBooks(db).then(books => {
    res.status(200).send(books);
    db.close();
  });
});


// MATH BOOKS
app.post('/new-book', (req, res) => {
  const db = new sqlite3.Database('mathapp.db');
  mathBooksModule.addNewBook(req.body, db).then(message => {
    res.status(200).send(message);
    db.close();
  });
});

app.get('/books', async (req, res) => {
  const db = new sqlite3.Database('mathapp.db');
  const books = await mathBooksModule.getListOfBooks(db);
  res.status(200).send(books);
  db.close();
});

app.get('/all-books-details', async (req, res) => {
  const db = new sqlite3.Database('mathapp.db');
  const books = await mathBooksModule.getListOfBooks(db);
  for (let book of books) {
    book['chapters'] = await mathBooksModule.getChaptersWithSubchaptersBy(book.id, db);
  }
  res.status(200).send(books);
  db.close();
});

// CHAPTERS
app.get('/book-chapters', (req, res) => {
  const db = new sqlite3.Database('mathapp.db');
  mathBooksModule.getChaptersWithSubchaptersBy(req.query.bookId, db).then(chapters => {
    res.status(200).send(chapters);
    db.close();
  });
});

app.put('/subchapters', (req, res) => {
  const db = new sqlite3.Database('mathapp.db');
  Object.keys(req.body).forEach(key => {
    db.run(`UPDATE subchapters SET ${key}=${req.body[key]} WHERE id=${req.query.id};`, () => {
      res.send('subchapter updated');
    });
  });
  db.close();
});

// EXERCISES
app.get('/exercises', (req, res) => {
  const db = new sqlite3.Database('mathapp.db');
  mathBooksModule.getExercise(req.query, db).then(exercise => {
    res.status(200).send(exercise);
    db.close();
  });
});

app.post('/exercises', (req, res) => {
  const db = new sqlite3.Database('mathapp.db');
  mathBooksModule.addNewExercise(req.body, db).then(message => {
    res.status(200).send(message);
    db.close();
  });
});



