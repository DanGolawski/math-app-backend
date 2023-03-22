from flask import Flask, request
app = Flask(__name__)
from sql_service import *
from math_book_service import *

@app.route('/')
def hello():
    return 'Hello!'

# RECOMMENDED VIDEOS
@app.route('/recommended-videos', methods=['POST'])
def add_recommended_video():
    new_video = request.json
    sql_code = f'INSERT INTO recommendedvideos (author, title, url) VALUES ("{new_video["author"]}", "{new_video["title"]}", "{new_video["url"]}");'
    return execute_sql_insert_with_response(sql_code, True)

@app.route('/recommended-videos', methods=['GET'])
def get_recommended_videos():
    sql_code = 'SELECT * FROM recommendedvideos'
    return execute_sql_select_with_response(sql_code, True)

# RECOMMENDED BOOKS
@app.route('/recommended-books', methods=['POST'])
def add_recommended_books():
    new_book = request.json
    sql_code = f'INSERT INTO recommendedbooks (author, title, imageUrl) VALUES ("{new_book["author"]}", "{new_book["title"]}", "{new_book["imageUrl"]}");'
    return execute_sql_insert_with_response(sql_code, True)

@app.route('/recommended-books', methods=['GET'])
def get_recommended_books():
    sql_code = 'SELECT * FROM recommendedbooks;'
    return execute_sql_select_with_response(sql_code, True)

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

@app.route('/books', methods=['GET'])
def get_books():
    sql_code = 'SELECT * FROM books;'
    return execute_sql_select_with_response(sql_code, True)


# CHAPTERS
@app.route('/chapters', methods=['GET'])
def get_chapters_with_subchapters_for_book():
    book_id = request.args.get('bookId')
    return get_chapters_with_subchapters(book_id)

# DO DOKONCZENIA
# @app.route('/subchapters', methods=['PUT'])
# def update_subchapter_data():
#     subchapter = request.json
#     for key in subchapter:
#         print(key)
#     return 'done', 200

# EXERCISES
@app.route('/exercises', methods=['POST'])
def add_new_exercise():
    print(request.json['bookId'])
    exercise = request.json
    sql_code = f'INSERT INTO exercises (bookId, chapterNumber, subchapterNumber, number, imageUrl, videoUrl, identifier) VALUES ("{exercise["bookId"]}", {exercise["chapterNumber"]}, {exercise["subchapterNumber"]}, {exercise["number"]}, "{exercise["imageUrl"]}", "{exercise["videoUrl"]}", "{exercise["bookId"]}_{exercise["chapterNumber"]}_{exercise["subchapterNumber"]}")'
    return execute_sql_insert_with_response(sql_code, True)

@app.route('/exercises', methods=['GET'])
def get_exercises():
    book_id = request.args.get('bookId')
    chapter_number = request.args.get('chapterNumber')
    subchapter_number = request.args.get('subchapterNumber')
    exercise_number = request.args.get('number')
    sql_code = f'SELECT * FROM exercises WHERE bookId="{book_id}" AND chapterNumber={chapter_number} AND subchapterNumber={subchapter_number} AND number={exercise_number}'
    return execute_sql_select_with_response(sql_code, True)

if __name__ == "__main__":
    app.run()
