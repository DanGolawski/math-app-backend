function getVideos(db) {
  return new Promise((resolve, reject) => {
    db.all('SELECT * FROM videos;', [], (err, rows) => {
      if (err) {
        throw err;
      }
      resolve(rows);
    });
  });
}

function addNewVideo(requestBody, db) {
  return new Promise((resolve, reject) => {
    db.run(`INSERT INTO videos (author, title, url) VALUES ("${requestBody.author}", "${requestBody.title}", "${requestBody.url}");`, () => {
      resolve('video added');
    });
  })
}

function addNewRecommendedBook(book, db) {
  return new Promise((resolve, reject) => {
    db.run(`INSERT INTO recommendedbooks (author, title, imageUrl) VALUES ("${book.author}", "${book.title}", "${book.imageUrl}");`, () => {
      resolve('new book added');
    });
  });
}

function getRecommendedBooks(db) {
  return new Promise((resolve, reject) => {
    db.all('SELECT * FROM recommendedbooks;', [], (err, rows) => {
      if (err) {
        throw err;
      }
      resolve(rows);
    });
  });
}

module.exports = {
  getVideos,
  addNewVideo,
  addNewRecommendedBook,
  getRecommendedBooks
}