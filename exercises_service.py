import sql_service
import shared
from werkzeug.utils import secure_filename
import os
import email_handler

def add_new_exercise(exercise_data, exercise_image):
    add_exercise_data(exercise_data)
    if exercise_image != None:
        image_name = f'{exercise_data["subchapterid"]}_{exercise_data["number"]}.png'
        add_exercise_image(exercise_image, image_name)
    return 'added'

def add_exercise_data(exercise_data):
    data_without_none = { key: value for key, value in exercise_data.items() if value is not None }
    keys = ','.join(data_without_none.keys())
    values = shared.map_to_sql_row_values(data_without_none.values())
    sql_query = f'INSERT INTO exercises ({keys}) VALUES ({values});'
    return sql_service.execute_sql_insert(sql_query)
    
def add_exercise_image(exercise_image, image_name):
    filename = secure_filename(image_name)
    exercise_image.save(os.path.join('EXERCISES', filename))

def get_exercises(subchapterid, number):
    sql_query = f"SELECT * FROM exercises WHERE subchapterid={subchapterid} AND number={number}"
    result = sql_service.execute_sql_select(sql_query)
    return result[0] if len(result) > 0 else ('', 204)

def send_exercise_request(exercise_data):
    sql_query = f'SELECT chapters.title as chapter, subchapters.title as subchapter FROM subchapters INNER JOIN chapters ON subchapters.chapterid = chapters.id WHERE subchapters.id = {exercise_data["subchapter"]}'
    result = sql_service.execute_sql_select(sql_query)
    data = result[0] if len(result) > 0 else None
    if (data == None):
        return 'no chapter or subchapter'
    message = email_handler.create_message(
        'mathmasters.contact@gmail.com',
        'Prosba o zadanie',
        f'ROZDZIAL: {data["chapter"]}, TEMAT: {data["subchapter"]}, ZADANIE: {exercise_data["exercise"]}'
    )
    email_handler.send_message(message)
    return 'done'
    
