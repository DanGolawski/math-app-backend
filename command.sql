CREATE TABLE exercises(
	id SERIAL PRIMARY KEY,
	subchapterid INT NOT NULL,
	number INT NOT NULL,
	image TEXT NOT NULL,
	video TEXT,
	UNIQUE(subchapterid, number)
);


CREATE TABLE books (
	id SERIAL PRIMARY KEY,
	title VARCHAR(1000) NOT NULL,
	UNIQUE(title)
);

CREATE TABLE chapters (
	id SERIAL PRIMARY KEY,
	bookid INT NOT NULL,
	number INT NOT NULL,
  title VARCHAR(500) NOT NULL,
	UNIQUE(bookid, number)
);

CREATE TABLE subchapters (
	id SERIAL PRIMARY KEY,
	chapterid INT NOT NULL,
	number INT NOT NULL,
	title VARCHAR(500),
  firstexercise INT NOT NULL,
  exercisesnumber INT NOT NULL,
	UNIQUE(chapterid, number)
);



