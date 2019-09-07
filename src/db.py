import sqlite3
from queries import CREATE_TABLE, SAVE_QUEUE, GET_QUEUE, UPDATE_QUEUE

DB_NAME = 'db.db'

def start_database():
    connection = __create_connection()
    __seed(connection)

def save_queue(queue, body):
    try:
        connection = __create_connection()
        connection.cursor().execute(SAVE_QUEUE, (queue, body))
        connection.commit()
        connection.close()
    except NameError as e:
        raise NameError('Error to save queue: ' + str(e))

def update_queue(queue, body):
    try:
        connection = __create_connection()
        connection.cursor().execute(UPDATE_QUEUE, (body, queue))
        connection.commit()
        connection.close()
    except NameError as e:
        raise NameError('Error to update queue: ' + str(e))

def get_queue_json(queue):
    try:
        connection = __create_connection()
        result = connection.cursor().execute(GET_QUEUE, (queue,))
        json_result = result.fetchone()[0]
        connection.close()
        return json_result
    except NameError as e:
        raise NameError('Error to get query: ' + str(e))

def __create_connection():
    try:
        return sqlite3.connect(DB_NAME)
    except:
        raise NameError('Error to connect to the database')

def __seed(connection):
    try:
        connection.cursor().execute(CREATE_TABLE)
        connection.commit()
        connection.close()
    except NameError as e:
        raise NameError('Error to create table queues: ' + str(e))