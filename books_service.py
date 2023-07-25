import sql_service

def add_book(title):
    sql_code = f"INSERT INTO books (title) VALUES ({title});"
    sql_service.execute_sql_insert(sql_code)
    return 'added'

def get_books():
    return sql_service.execute_sql_select('SELECT * FROM books')

def get_chapters_with_subchapters_by(bookid):
    sql_query = f"SELECT chapters.number, chapters.title, subchapters.id, subchapters.number as subchapternumber, subchapters.title as subchaptertitle, subchapters.firstexercise, subchapters.exercisesnumber FROM chapters LEFT JOIN subchapters ON chapters.id = subchapters.chapterid WHERE chapters.bookid = {bookid} ORDER BY chapters.number;"
    chapters_and_subchapters = sql_service.execute_sql_select(sql_query)
    chapter_objects = []
    curr_chapter_number = None
    for record in chapters_and_subchapters:
        if record['number'] != curr_chapter_number:
            curr_chapter_number = record['number']
            chapter_objects.append({
                'number': record['number'],
                'title': record['title'],
                'subchapters': [],
            })
        add_subchapter_to_chapter(chapter_objects[-1], record)
    return chapter_objects

def add_subchapter_to_chapter(current_chapter, db_row):
    if db_row['id'] == None:
        return
    current_chapter['subchapters'].append({
        'id': db_row['id'],
        'number': db_row['subchapternumber'],
        'title': db_row['subchaptertitle'],
        'firstexercise': db_row['firstexercise'],
        'exercisesnumber': db_row['exercisesnumber']    
    })

