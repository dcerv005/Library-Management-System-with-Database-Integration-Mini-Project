import mysql.connector
from mysql.connector import Error

def connect_database():
    db_name = 'library_management_db'
    user= 'root'
    password = 'Dc418289!'
    host = 'localhost'

    try:
        conn = mysql.connector.connect(
            database= db_name,
            user = user,
            password=password,
            host=host
        )

        if conn.is_connected():
            print(f'Connected to database: {db_name}.')
            return conn
        
    except Error as e:
        print(f'Error: {e}')
        return None