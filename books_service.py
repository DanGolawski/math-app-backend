import sql_service

def add_book(title):
    sql_code = f"INSERT INTO books (title) VALUES ({title});"
    sql_service.execute_sql_insert(sql_code)
    return 'added'

def get_books():
    return sql_service.execute_sql_select('SELECT * FROM books')

def get_chapters_with_subchapters_by(bookid):
    sql_query = f"SELECT chapters.number, chapters.title, subchapters.id, subchapters.number as subchapternumber, subchapters.title as subchaptertitle FROM chapters LEFT JOIN subchapters ON chapters.id = subchapters.chapterid WHERE chapters.bookid = {bookid} ORDER BY chapters.number;"
    chapters_and_subchapters = sql_service.execute_sql_select(sql_query)
    chapter_objects = []
    curr_chapter_number = None
    for record in chapters_and_subchapters:
        if record['number'] == curr_chapter_number:
            chapter_objects[-1]['subchapters'].append({'id': record['id'], 'number': record['subchapternumber'], 'title': record['subchaptertitle']})
        else:
            curr_chapter_number = record['number']
            chapter_objects.append({
                'number': record['number'],
                'title': record['title'],
                'subchapters': [],
            })
    return chapter_objects