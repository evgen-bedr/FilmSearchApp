import mysql.connector

# Конфигурация для 1 базы данных
dbconfig_films = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'movies'
}

# Конфигурация для 2 базы данных
dbconfig_search = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'frequency_main'
}

def get_connection_films():
    try:
        connection = mysql.connector.connect(**dbconfig_films)
        print('Соединение с БД фильмов прошло успешно')
        return connection
    except mysql.connector.Error as e:
        print(f'Ошибка соединения с БД 1: {e}')
        return None

def get_connection_search():
    try:
        connection = mysql.connector.connect(**dbconfig_search)
        print('Соединение с БД поиска прошло успешно')
        return connection
    except mysql.connector.Error as e:
        print(f'Ошибка соединения с БД 2: {e}')
        return None

def execute_query(query, params=None):
    connection = get_connection_films()
    return execute_query_common(connection, query, params)

def execute_query_search(query, params=None):
    connection = get_connection_search()
    return execute_query_common(connection, query, params)

def execute_query_common(connection, query, params):
    if connection is None:
        return [], []
    cursor = connection.cursor()
    try:
        cursor.execute(query, params or ())
        results = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        return results, column_names
    except mysql.connector.Error as err:
        print(f"Ошибка в базе данных: {err}")
        return [], []
    finally:
        cursor.close()
        connection.close()
