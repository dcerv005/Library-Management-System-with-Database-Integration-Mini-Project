from open_database import connect_database

def add_genre(name, description):
    conn = connect_database()
    if conn is not None:
        try:
            cursor=conn.cursor()
            query='SELECT name FROM Genres'
            cursor.execute(query)
            genres=[x[0] for x in cursor.fetchall()]#Putting all genres in a list
            if name not in genres:
                query= 'INSERT INTO Genres (name, description) VALUES(%s, %s)'
                genre= (name, description)          
                cursor.execute(query, genre)
                conn.commit()
                print('Genre added')
            else:
                print('Genre exists')
            new_query = 'SELECT id FROM Genres WHERE name = %s'
            cursor.execute(new_query, (name, ))
            id=[x[0] for x in cursor.fetchall()]
            return id[0]
        except Exception as e:
            print(f"Error: {e}")
        finally:
            conn.close()
            cursor.close()

def search_genre(name):    
    conn = connect_database()
    if conn is not None:
        try:
            cursor=conn.cursor()
            query= 'SELECT * FROM Genres WHERE name = %s'
            cursor.execute(query, (name, ))
            genre=cursor.fetchall()
            if genre:
                print(genre[0])
            else: 
                print('Genre does not exist.')
            
        except Exception as e:
            print(f'Error: {e}')
        finally:
            conn.close()
            cursor.close()

def display_genres():
    conn = connect_database()
    if conn is not None:
        try:
            cursor=conn.cursor()
            query = 'SELECT * FROM Genres'
            cursor.execute(query)
            for row in cursor.fetchall():
                print(row)

        except Exception as e:
            print(f'Error: {e}')
        
        finally:
            conn.close()
            cursor.close()
