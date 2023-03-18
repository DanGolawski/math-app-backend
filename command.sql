-- CREATE TABLE books(
--   id VARCHAR(255) NOT NULL UNIQUE,
--   title VARCHAR(255) NOT NULL UNIQUE
-- );

-- CREATE TABLE chapters(
--   id INTEGER PRIMARY KEY,
--   bookId VARCHAR(255) NOT NULL,
--   number INTEGER NOT NULL,
--   name VARCHAR(255) NOT NULL
-- );

-- CREATE TABLE subchapters(
--   id INTEGER PRIMARY KEY,
--   bookId VARCHAR(255) NOT NULL,
--   chapterNumber INTEGER NOT NULL,
--   number INTEGER NOT NULL,
--   name VARCHAR(255) NOT NULL,
--   numberOfExercises INTEGER NOT NULL,
--   firstExerciseNumber INTEGER NOT NULL
-- );

-- CREATE TABLE exercises(
--   id INTEGER PRIMARY KEY,
--   bookId VARCHAR(255) NOT NULL,
--   chapterNumber INTEGER NOT NULL,
--   subchapterNumber INTEGER NOT NULL,
--   number INTEGER NOT NULL,
--   imageUrl VARCHAR(255) NOT NULL
-- );

-- CREATE TABLE recommendedbooks(
--   id INTEGER PRIMARY KEY,
--   title VARCHAR(255),
--   author VARCHAR(255),
--   imageUrl VARCHAR(255)
-- );

-- DELETE FROM books;
-- DELETE FROM chapters;
-- DELETE FROM subchapters;
-- DELETE FROM exercises;
-- DELETE FROM videos;
-- DELETE FROM recommendedbooks;

