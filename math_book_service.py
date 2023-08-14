from sql_service import *

def insert_new_book(book):
    book_sql_code = f"INSERT INTO books (id, title) VALUES ('{book['id']}', '{book['title']}')"
    return execute_sql_insert_with_response(book_sql_code, False)
    
    
def insert_new_chapter(book_id, chapter):
    chapter_sql_code = f"INSERT INTO chapters (bookId, number, name, identifier) VALUES ('{book_id}', '{chapter['number']}', '{chapter['name']}', '{book_id}_{chapter['number']}')"
    return execute_sql_insert_with_response(chapter_sql_code, False)
    
    
def insert_new_subchapter(book_id, chapter_number, subchapter):
    subchapter_sql_code = f"INSERT INTO subchapters (bookId, chapterNumber, number, name, numberOfExercises, firstExerciseNumber, identifier) VALUES ('{book_id}', {chapter_number}, {subchapter['number']}, '{subchapter['name']}', {subchapter['numberOfExercises']}, {subchapter['firstExerciseNumber']}, '{book_id}_{chapter_number}_{subchapter['number']}')"
    return execute_sql_insert_with_response(subchapter_sql_code, False)

def get_chapters_with_subchapters(book_id):
    chapters_sql_code = f"SELECT * FROM chapters WHERE bookId='{book_id}'"
    try:
        chapters = execute_sql_select(chapters_sql_code)
        for chapter in chapters:
            chapter['subchapters'] = execute_sql_select(f"SELECT * FROM subchapters WHERE bookId='{book_id}' AND chapterNumber={chapter['number']}")
        return jsonify(chapters), 200
    except psycopg2.Error as error:
        print('ERROR OCCURED', error)
        return f'{error}', 400
