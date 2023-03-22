-- DROP TABLE books;
-- DROP TABLE chapters;
-- DROP TABLE subchapters;
-- DROP TABLE exercises;
-- DROP TABLE videos;
-- DROP TABLE recommendedbooks;
-- DROP TABLE recommendedvideos;

-- CREATE TABLE books(
--   id VARCHAR(255) NOT NULL UNIQUE,
--   title VARCHAR(255) NOT NULL UNIQUE
-- );

-- CREATE TABLE chapters(
--   id INTEGER PRIMARY KEY,
--   bookId VARCHAR(255) NOT NULL,
--   number INTEGER NOT NULL,
--   name VARCHAR(255) NOT NULL,
--   identifier VARCHAR(255) NOT NULL UNIQUE
-- );

-- CREATE TABLE subchapters(
--   id INTEGER PRIMARY KEY,
--   bookId VARCHAR(255) NOT NULL,
--   chapterNumber INTEGER NOT NULL,
--   number INTEGER NOT NULL,
--   name VARCHAR(255) NOT NULL,
--   numberOfExercises INTEGER NOT NULL,
--   firstExerciseNumber INTEGER NOT NULL,
--   identifier VARCHAR(255) NOT NULL UNIQUE
-- );

-- CREATE TABLE exercises(
--   id INTEGER PRIMARY KEY,
--   bookId VARCHAR(255) NOT NULL,
--   chapterNumber INTEGER NOT NULL,
--   subchapterNumber INTEGER NOT NULL,
--   number INTEGER NOT NULL,
--   imageUrl VARCHAR(255) NOT NULL,
--   videoUrl VARCHAR(255) NOT NULL,
--   identifier VARCHAR(255) NOT NULL UNIQUE
-- );

-- CREATE TABLE recommendedbooks(
--   id INTEGER PRIMARY KEY,
--   title VARCHAR(255) NOT NULL UNIQUE,
--   author VARCHAR(255) NOT NULL,
--   imageUrl VARCHAR(255) NOT NULL UNIQUE
-- );

-- CREATE TABLE recommendedvideos(
--    id INTEGER PRIMARY KEY,
--    title VARCHAR(255),
--    author VARCHAR(255),
--    url VARCHAR(255) UNIQUE
-- )

-- DELETE FROM books;
-- DELETE FROM chapters;
-- DELETE FROM subchapters;
-- DELETE FROM exercises;
-- DELETE FROM videos;
-- DELETE FROM recommendedbooks;
-- DELETE FROM recommendedvideos

