function getListOfBooks(db) {
  return new Promise((resolve, reject) => {
    db.all('SELECT * from books;', (err, rows) => {
      if (err) throw err;
      resolve(rows); 
    })
  });
}

function getChaptersBy(bookId, db) {
  return new Promise((resolve, reject) => {
    db.all(`SELECT name, number from chapters WHERE bookId = "${bookId}";`, (err, rows) => {
      if (err) throw err;
      resolve(rows); 
    })
  });
}

async function getChaptersWithSubchaptersBy(bookId, db) {
  const chapters = await getChaptersBy(bookId, db);
  for (let chapter of chapters) {
    chapter['subchapters'] = await getSubchaptersBy(chapter.number, bookId, db);
  }
  chapters.sort((chapter1, chapter2) => chapter1.number - chapter2.number);
  return chapters;
}

function getSubchaptersBy(chapterNumber, bookId, db) {
  return new Promise((resolve, reject) => {
    db.all(`SELECT * FROM subchapters WHERE chapterNumber=${chapterNumber} AND bookId="${bookId}";`, (err, subchapters) => {
      if (err) throw err;
      subchapters.sort((sub1, sub2) => sub1.number - sub2.number);
      resolve(subchapters);
    });
  });
}

function addNewBook(book, db) {
  return new Promise((resolve, reject) => {
    db.run(`INSERT INTO books (id, title) VALUES ("${book.id}", "${book.title}");`, [], err => reject(err));
    for(let chapter of book.chapters) {
      db.run(`INSERT INTO chapters (bookId, number, name) VALUES ("${book.id}", "${chapter.number}", "${chapter.name}");`);
      for(let subchapter of chapter.subchapters) {
        db.run(`INSERT INTO subchapters (bookId, chapterNumber, number, name, numberOfExercises, firstExerciseNumber) VALUES ("${book.id}", ${chapter.number}, ${subchapter.number}, "${subchapter.name}", ${subchapter.numberOfExercises}, ${subchapter.firstExerciseNumber});`);
      }
    }
    resolve('new book added');
  });
}

function getExercise(filterValues, db) {
  return new Promise((resolve, reject) => {
    db.all(`SELECT number, imageUrl FROM exercises WHERE bookId="${filterValues.book}" AND chapterNumber=${filterValues.chapter} AND subchapterNumber=${filterValues.subchapter} AND number=${filterValues.number};`, (err, results) => {
      if (err) throw err;
      if (results.length) {
        resolve(results[0]);
      } else {
        resolve({});
      }
    });
  });
}

function addNewExercise(exerciseData, db) {
  return new Promise((resolve, reject) => {
    db.run(`INSERT INTO exercises (bookId, chapterNumber, subchapterNumber, number, imageUrl) VALUES ("${exerciseData.book}", ${exerciseData.chapter}, ${exerciseData.subchapter}, ${exerciseData.number}, "${exerciseData.imageUrl}");`);
    resolve('exercise added');
  });
}

module.exports = {
  getListOfBooks,
  getChaptersBy,
  getSubchaptersBy,
  getChaptersWithSubchaptersBy,
  addNewBook,
  getExercise,
  addNewExercise
}