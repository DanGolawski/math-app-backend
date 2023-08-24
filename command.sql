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
INSERT INTO books (title) VALUES ('Matematyka Pazdro 2019 kl. 1, p. rozszerzony');
INSERT INTO books (title) VALUES ('Matematyka Pazdro 2019 kl. 2, p. rozszerzony');
INSERT INTO books (title) VALUES ('Matematyka Pazdro 2019 kl. 3, p. rozszerzony');
INSERT INTO books (title) VALUES ('Matematyka Pazdro 2019 kl. 4, p. rozszerzony');
INSERT INTO books (title) VALUES ('Matematyka Nowa Era kl. 1');
INSERT INTO books (title) VALUES ('Matematyka Nowa Era kl. 2');
INSERT INTO books (title) VALUES ('Matematyka Nowa Era kl. 3');
INSERT INTO books (title) VALUES ('Matematyka Nowa Era kl. 4');

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



INSERT INTO CHAPTERS (bookid, number, title) VALUES (2, 1, 'Przekształcenia wykresów funkcji');
INSERT INTO CHAPTERS (bookid, number, title) VALUES (2, 2, 'Równania i nierówności z wartością bezwzględną');
INSERT INTO CHAPTERS (bookid, number, title) VALUES (2, 3, 'Funkcja kwadratowa');
INSERT INTO CHAPTERS (bookid, number, title) VALUES (2, 4, 'Geometria płaska - okręgi i koła');
INSERT INTO CHAPTERS (bookid, number, title) VALUES (2, 5, 'Trygonometria');
INSERT INTO CHAPTERS (bookid, number, title) VALUES (2, 6, 'Geometria analityczna');
INSERT INTO CHAPTERS (bookid, number, title) VALUES (2, 7, 'Geometria płaska - rozwiązywanie trójkątów, pole trójkąta, pole koła');
INSERT INTO CHAPTERS (bookid, number, title) VALUES (2, 8, 'Wielomiany');

INSERT INTO subchapters (chapterid, number, title, firstexercise, exercisesnumber) VALUES (1, 1, 'Wektor w układzie współrzędnych - podstawowe informacje', 1, 32);
INSERT INTO subchapters (chapterid, number, title, firstexercise, exercisesnumber) VALUES (1, 2, 'Przesunięcie równoległe. Przesunięcie równoległe wzdłuż osi OX', 33, 19);
INSERT INTO subchapters (chapterid, number, title, firstexercise, exercisesnumber) VALUES (1, 3, 'Przesunięcie równoległe wzdłuż osi OY', 52, 28);
INSERT INTO subchapters (chapterid, number, title, firstexercise, exercisesnumber) VALUES (1, 4, 'Symetria osiowa. Symetria osiowa względem osi OX i OY', 80, 17);
INSERT INTO subchapters (chapterid, number, title, firstexercise, exercisesnumber) VALUES (1, 5, 'Symetria środkowa. Symetria środkowa względem punktu (0,0)', 97, 8);
INSERT INTO subchapters (chapterid, number, title, firstexercise, exercisesnumber) VALUES (1, 6, 'Wykres funkcji y = |f(x)| oraz y = f(|x|)', 105, 16);
INSERT INTO subchapters (chapterid, number, title, firstexercise, exercisesnumber) VALUES (1, 7, 'Wykres funkcji y = kf(x) oraz y = f(kx), gdzie k = 0', 121, 16);
INSERT INTO subchapters (chapterid, number, title, firstexercise, exercisesnumber) VALUES (1, 8, 'Szkicowanie wykresów wybranych funkcji', 137, 17);
INSERT INTO subchapters (chapterid, number, title, firstexercise, exercisesnumber) VALUES (1, 9, 'Zastosowanie wykresów funkcji do rozwiązywania równań i nierówności', 154, 18);
INSERT INTO subchapters (chapterid, number, title, firstexercise, exercisesnumber) VALUES (1, 10, 'Zadania powtórzeniowe do rozdziału 1.', 16, 26);

INSERT INTO subchapters (chapterid, number, title, firstexercise, exercisesnumber) VALUES (7, 1, 'Twierdzenie sinusów',1,13);
INSERT INTO subchapters (chapterid, number, title, firstexercise, exercisesnumber) VALUES (7, 2, 'Twierdzenie cosinusów',14,16);
INSERT INTO subchapters (chapterid, number, title, firstexercise, exercisesnumber) VALUES (7, 3, 'Zastosowanie twierdzenia sinusów i twierdzenia cosinusów do rozwiązywania zadań',30,18);
INSERT INTO subchapters (chapterid, number, title, firstexercise, exercisesnumber) VALUES (7, 4, 'Pole figury płaskiej',48,2);
INSERT INTO subchapters (chapterid, number, title, firstexercise, exercisesnumber) VALUES (7, 5, 'Pole trójkąta, cz. 1',50,37);
INSERT INTO subchapters (chapterid, number, title, firstexercise, exercisesnumber) VALUES (7, 6, 'Pole trójkąta, cz. 2',87,23);
INSERT INTO subchapters (chapterid, number, title, firstexercise, exercisesnumber) VALUES (7, 7, 'Pola trójkątów podobnych',110,21);
INSERT INTO subchapters (chapterid, number, title, firstexercise, exercisesnumber) VALUES (7, 8, 'Pole koła, pole wycinka koła',131,14);
INSERT INTO subchapters (chapterid, number, title, firstexercise, exercisesnumber) VALUES (7, 9, 'Zastosowanie pojęcia pola w dowodzeniu twierdzeń',145,12);
INSERT INTO subchapters (chapterid, number, title, firstexercise, exercisesnumber) VALUES (7, 10, 'Zadania powtórzeniowe do rozdziału 7.',16,25);
