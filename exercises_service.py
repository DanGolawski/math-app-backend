import sql_service
import shared
import os
import uuid
import email_handler
import io
import base64
from PIL import Image

def add_new_exercise(exercise_data, exercise_image):
    if exercise_image == None:
        return 'no image', 404
    filename = str(uuid.uuid4())
    add_exercise_data(exercise_data, filename)
    add_exercise_image(exercise_image, filename)
    return 'added'

def add_exercise_data(exercise_data, filename):
    exercise_data['image'] = filename
    exercise_data['video'] = extract_video_id(exercise_data.get('video', None))
    data_without_none = { key: value for key, value in exercise_data.items() if value is not None }
    keys = ','.join(data_without_none.keys())
    values = shared.map_to_sql_row_values(data_without_none.values())
    sql_query = f'INSERT INTO exercises ({keys}) VALUES ({values})'
    sql_service.execute_sql_insert(sql_query)

def extract_video_id(embed_link):
    if embed_link == None:
        return None
    return embed_link.split('/')[-1]
    
def add_exercise_image(exercise_image, filename):
    exercise_image.save(os.path.join('EXERCISES', f'{filename}.png'))
    return filename

def get_exercises(subchapterid, number):
    sql_query = f"SELECT image, video FROM exercises WHERE subchapterid={subchapterid} AND number={number}"
    result = sql_service.execute_sql_select(sql_query)
    if len(result) == 0:
        return ('', 204)
    result = result[0]
    result['image'] = get_encoded_img(result['image'])
    return result

def get_encoded_img(filename):
    img = Image.open(f'./EXERCISES/{filename}.png', mode='r')
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    encoded_img = base64.encodebytes(img_byte_arr.getvalue()).decode('ascii')
    return encoded_img

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
    
