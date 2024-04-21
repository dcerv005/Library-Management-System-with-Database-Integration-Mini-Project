from open_database import connect_database

def add_book(title, author_id, genre_id, isbn, publication_date):    
    conn = connect_database()
    if conn is not None:
        try:
            cursor=conn.cursor()
            query='SELECT title FROM Books'
            cursor.execute(query)
            books=[x[0] for x in cursor.fetchall()]#Putting all books in a list
            if title not in books:

                query= 'INSERT INTO Books (title, author_id, genre_id, isbn, publication_date) VALUES(%s, %s, %s, %s, %s)'
                book= (title, author_id, genre_id, isbn, publication_date)          
                cursor.execute(query, book)
                conn.commit()
                print('Book added')
            else:
                print('Book exists')
        except Exception as e:
            print(f'Error: {e}')
        finally:
            conn.close()
            cursor.close()

def borrowed_books(user, book, borrowed_date):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            availability_query= 'SELECT availability FROM Books WHERE title = %s'
            cursor.execute(availability_query, (book, ))
            a=[x[0] for x in cursor.fetchall()]
            if a[0] == 1:                
                user_query = 'SELECT id FROM Users WHERE library_id = %s'
                cursor.execute(user_query, (user, ))
                user_id=[x[0] for x in cursor.fetchall()]
                book_query= 'SELECT id FROM Books WHERE title = %s'
                cursor.execute(book_query, (book, ))
                book_id=[x[0] for x in cursor.fetchall()]
                borrowed_book_query = 'INSERT INTO Borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, %s)'
                cursor.execute(borrowed_book_query, (user_id[0], book_id[0], borrowed_date))
                conn.commit()
                print(f'Book, {book}, has been borrowed')
                change_availability= 'UPDATE Books SET availability = %s WHERE id = %s'
                cursor.execute(change_availability, (0, book_id[0]))
                conn.commit()
            else:
                print(f'Book: {book}, is not available.')
            
            
        except Exception as e:
            print(f'Error: {e}')
        finally:
            conn.close()
            cursor.close()

def return_book(user, book, return_date):
    conn = connect_database()
    if conn is not None:
        try:
            cursor=conn.cursor()
            availability_query= 'SELECT availability FROM Books WHERE title = %s'
            cursor.execute(availability_query, (book, ))
            a=[x[0] for x in cursor.fetchall()]
            if a[0] == 0:
                user_query = 'SELECT id FROM Users WHERE library_id = %s'
                cursor.execute(user_query, (user, ))
                user_id=[x[0] for x in cursor.fetchall()]
                book_query= 'SELECT id FROM Books WHERE title = %s'
                cursor.execute(book_query, (book, ))
                book_id=[x[0] for x in cursor.fetchall()]
                return_book_query= 'UPDATE Borrowed_books SET return_date = %s WHERE user_id= %s AND book_id = %s'
                cursor.execute(return_book_query, (return_date, user_id[0], book_id[0]))
                conn.commit()
                print(f'Book, {book}, has been returned.')
                change_availability= 'UPDATE Books SET availability = %s WHERE id = %s'
                cursor.execute(change_availability, (1, book_id[0]))
                conn.commit()
            else:
                print(f'Book, {book}, was not borrowed.')
        except Exception as e:
            print(f'Error: {e}')
        finally:
            conn.close()
            cursor.close()
def search_book(book_title):
    conn = connect_database()
    if conn is not None:
        try:
            cursor=conn.cursor()
            query= 'SELECT * FROM Books WHERE title = %s'
            cursor.execute(query, (book_title, ))
            book=cursor.fetchall()
            if book:
                print(book[0])
            else: 
                print('Book does not exist.')
            
        except Exception as e:
            print(f'Error: {e}')
        finally:
            conn.close()
            cursor.close()
def display_books():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = 'SELECT * FROM Books'
            cursor.execute(query)
            for row in cursor.fetchall():
                print(row)
        except Exception as e:
            print(f'Error: {e}')
        finally:
            conn.close()
            cursor.close()