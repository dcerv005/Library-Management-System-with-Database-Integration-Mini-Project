from open_database import connect_database

def add_user(name, library_id):
    conn = connect_database()
    if conn is not None:
        try:
            cursor=conn.cursor()
            query = 'INSERT INTO Users (name, library_id) VALUES(%s, %s)'
            cursor.execute(query, (name, library_id))
            conn.commit()
            print('User added.')
        except Exception as e:
            print(f'Error: {e}')
        finally:
            conn.close()
            cursor.close()

def search_user(library_id):
    conn = connect_database()
    if conn is not None:
        try:
            cursor=conn.cursor()
            query= 'SELECT * FROM Users WHERE library_id = %s'
            cursor.execute(query, (library_id, ))
            user =cursor.fetchall()
            if user:
                print(user[0])
            else: 
                print('User does not exist.')
            
        except Exception as e:
            print(f'Error: {e}')
        finally:
            conn.close()
            cursor.close()
def display_users():
    conn = connect_database()
    if conn is not None:
        try:
            cursor=conn.cursor()
            query = 'SELECT * FROM Users'
            cursor.execute(query)
            for row in cursor.fetchall():
                print(row)

        except Exception as e:
            print(f'Error: {e}')
        
        finally:
            conn.close()
            cursor.close()