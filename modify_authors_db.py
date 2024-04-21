from open_database import connect_database

def add_authors(name, bio):
    conn = connect_database()
    if conn is not None:
        try:
            cursor=conn.cursor()
            query='SELECT name FROM Authors'
            cursor.execute(query)
            authors=[x[0] for x in cursor.fetchall()]#Putting all authors in a list
            if name not in authors:

                query= 'INSERT INTO Authors (name, biography) VALUES(%s, %s)'
                author= (name, bio)          
                cursor.execute(query, author)
                conn.commit()
                print('Author added')
            else:
                print('Author exists')
            new_query = 'SELECT id FROM Authors WHERE name = %s'
            cursor.execute(new_query, (name, ))
            id=[x[0] for x in cursor.fetchall()]
            return id[0]
        except Exception as e:
            print(f'Error: {e}')
        finally:
            conn.close()
            cursor.close()

def search_author(name):
    conn = connect_database()
    if conn is not None:
        try:
            cursor=conn.cursor()
            query= 'SELECT * FROM Authors WHERE name = %s'
            cursor.execute(query, (name, ))
            authors=cursor.fetchall()
            if authors:
                print(authors[0])
            else: 
                print('Author does not exist.')
            
        except Exception as e:
            print(f'Error: {e}')
        finally:
            conn.close()
            cursor.close()

def display_authors():
    conn = connect_database()
    if conn is not None:
        try:
            cursor=conn.cursor()
            query = 'SELECT * FROM Authors'
            cursor.execute(query)
            for row in cursor.fetchall():
                print(row)
        except Exception as e:
            print(f'Error: {e}')
        finally:
            conn.close()
            cursor.close()
