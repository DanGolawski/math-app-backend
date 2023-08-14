from flask import Flask, request, jsonify, json
from sql_service import *
from math_book_service import *
import exercises_service
import books_service
from flask_cors import CORS
import sql_service

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Hello!'

# RECOMMENDED VIDEOS
@app.route('/recommended-videos', methods=['POST'])
def add_recommended_video():
    new_video = request.json
    sql_code = f"INSERT INTO recommendedvideos (author, title, url) VALUES ('{new_video['author']}', '{new_video['title']}', '{new_video['url']}')"
    return execute_sql_insert_with_response(sql_code, True)

@app.route('/recommended-videos', methods=['GET'])
def get_recommended_videos():
    sql_code = 'SELECT * FROM recommendedvideos'
    return execute_sql_select_with_response(sql_code, True)

@app.route('/recommended-videos/<videoId>', methods=['DELETE'])
def delete_recommended_video(videoId):
    sql_code = f'DELETE FROM recommendedvideos WHERE id={videoId}'
    return execute_sql_insert_with_response(sql_code, True)


# RECOMMENDED BOOKS
@app.route('/recommended-books', methods=['POST'])
def add_recommended_books():
    new_book = request.json
    sql_code = f"INSERT INTO recommendedbooks (author, title, imageUrl) VALUES ('{new_book['author']}', '{new_book['title']}', '{new_book['imageUrl']}')"
    return execute_sql_insert_with_response(sql_code, True)

@app.route('/recommended-books', methods=['GET'])
def get_recommended_books():
    sql_code = 'SELECT * FROM recommendedbooks'
    return execute_sql_select_with_response(sql_code, True)

@app.route('/recommended-books/<bookId>', methods=['DELETE'])
def delete_recommended_book(bookId):
    sql_code = f'DELETE FROM recommendedbooks WHERE id={bookId}'
    return execute_sql_insert_with_response(sql_code, True)

# MATH BOOKS
@app.route('/books', methods=['POST'])
def add_new_book():
    book = request.json
    errors = {'book': None, 'chapters': [], 'subchapters': []}
    errors['book'] = insert_new_book(book)
    for chapter in book['chapters']:
        print(f'inserting chapter: {chapter["name"]}')
        errors['chapters'].append(insert_new_chapter(book['id'], chapter))
        for subchapter in chapter['subchapters']:
            print(f'inserting subchapter: {subchapter["name"]}')
            errors['subchapters'].append(insert_new_subchapter(book['id'], chapter['number'], subchapter))
    return jsonify(errors), 200

#VIDEOS
@app.route('/videos', methods=['POST'])
def add_new_video():
    video = request.json
    sql_code = f"INSERT INTO videos (title, url) VALUES ('{video['title']}', '{video['url']}')"
    return execute_sql_insert_with_response(sql_code, True)

@app.route('/exercises-videos', methods=['POST'])
def add_new_exercise_video_relation():
    relation = request.json
    video_title = relation['videotitle']
    exercise = relation['exercise']
    video_id = execute_sql_select(f"SELECT id from videos WHERE title = '{video_title}'")
    if len(video_id) == 0:
        return 'No video found', 400
    exercise_id = execute_sql_select(f"SELECT id from exercises WHERE bookId = '{exercise['bookid']}' AND chapterNumber = {exercise['chapter']} AND subchapterNumber = {exercise['subchapter']} AND number = {exercise['number']}")
    if len(exercise_id) == 0:
        return 'No exercise found', 400
    sql_code = f"INSERT INTO exercise_video (exerciseid, videoid) VALUES ({exercise_id[0]['id']}, {video_id[0]['id']})"
    return execute_sql_insert_with_response(sql_code, True)

### BOOKS ###
@app.post('/books')
def add_book():
    book_title = request.json['title']
    try:
        return books_service.add_book(book_title)
    except psycopg2.Error as error:
        return f"{error}"

@app.get('/books')
def get_books():
    try:
        return books_service.get_books()
    except psycopg2.Error as error:
        return f"{error}", 400

@app.get('/books/chapters/<bookid>')
def get_chapters_for_book(bookid):
    try:
        return books_service.get_chapters_with_subchapters_by(bookid)
    except psycopg2.Error as error:
        return f"{error}", 400
    

### EXERCISES ###
@app.post('/exercises/add')
def add_new_exercise():
    try:
        request_json = json.loads(request.form.get('data'))
        request_image = request.files['image'] if 'image' in request.files else None
        return exercises_service.add_new_exercise(request_json, request_image)
    except psycopg2.Error as error:
        print(error)
        return f'{error}', 400

@app.get('/exercises/get/<subchapterid>/<number>')
def get_exercises(subchapterid, number):
    try:
        return exercises_service.get_exercises(subchapterid, number)
    except psycopg2.Error as error:
        print(error)
        return f'{error}', 400

@app.post('/exercises/request-solution')
def handle_exercise_request():
    exercise_details = request.json
    try:
        return exercises_service.send_exercise_request(exercise_details)
    except:
        print('blad podczas wysylania emaila', exercise_details['subchapter'], exercise_details['exercise'])
        return 'sending issue'

if __name__ == "__main__":
    sql_service.connect()
    app.run()
