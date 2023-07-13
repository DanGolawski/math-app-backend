import sql_service
import shared
from werkzeug.utils import secure_filename
import os

def add_new_exercise(exercise_data, exercise_image):
    add_exercise_data(exercise_data)
    if exercise_image != None:
        image_name = f'{exercise_data["bookid"]}_{exercise_data["chapter"]}_{exercise_data["subchapter"]}_{exercise_data["number"]}.png'
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

def get_exercises(subchapter, number):
    sql_query = f"SELECT * FROM exercises WHERE subchapter={subchapter} AND number={number}"
    result = sql_service.execute_sql_select(sql_query)
    return {
        'exercise': result[0] if len(result) > 0 else None
    }
