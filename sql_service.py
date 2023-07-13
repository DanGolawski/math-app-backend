from flask import jsonify
import psycopg2
import psycopg2.extras
import config

sqliteConnection = None

# funkcja aby sqlite zwracał dictionary zamiast values list https://stackoverflow.com/questions/3300464/how-can-i-get-dict-from-sqlite-query
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def execute_sql_insert_with_response(sql_code, status_code):
   try:
      execute_sql_insert(sql_code)
      if status_code:
         return 'Record inserted successfully into table', 200
      else:
         return 'Record inserted successfully into table'
   except psycopg2.Error as error:
      print("Failed to insert data into sqlite table", error)
      if status_code:
         return f'{error}', 400
      else:
         return f'{error}'
   finally:
      if sqliteConnection:
         sqliteConnection.close()
         print("The SQLite connection is closed")

def execute_sql_select_with_response(sql_code, status_code):
   try:
      records = execute_sql_select(sql_code)
      if status_code:
         return records, 200
      else:
         return records
   except psycopg2.Error as error:
      print('failed to read data:', error)
      if status_code:
         return f'{error}', 400
      else:
         return f'{error}'
   finally:
      if sqliteConnection:
         sqliteConnection.close()
         print('The SQLite connection is closed')

def execute_sql_insert(sql_code):
   print('start execution of INSERT method')
   connection, cursor = get_cursor()
   print("Successfully Connected to SQLite")
   cursor.execute(sql_code)
   connection.commit()
   print("Operation executed successfully")
   cursor.close()
   connection.close()

def execute_sql_select(sql_code):
   print('start execution of SELECT method')
   connection, cursor = get_cursor()
   print('Successfully Connected to SQLite')
   cursor.execute(sql_code)
   records = cursor.fetchall()
   cursor.close()
   connection.close()
   return jsonify(records).json

def get_cursor():
    connection = psycopg2.connect(
        host=config.DATABASE['host'],
        database=config.DATABASE['database'],
        user=config.DATABASE['user'],
        password=config.DATABASE['password']
    )
    cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    return connection, cursor
   