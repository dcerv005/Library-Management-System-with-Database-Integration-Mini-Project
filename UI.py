import modify_genres_db, modify_authors_db, modify_books_db, modify_users_db
from datetime import datetime

def book_operations():
    print("\nBook Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books")
    option = int(input("Please pick an option to continue: "))
    if option == 1:
        title = input('What is the title of the book being added? ').title()
        author = input('Enter auhtors name ').title()
        biography= input('Enter a biography for this author: ')
        author_id = modify_authors_db.add_authors(author, biography) 
        genre = input('Enter the genre name: ').title()
        description= input('Enter a description of the genre: ')
        genre_id = modify_genres_db.add_genre(genre, description)
        isbn=int(input('Please insert the book ISBN: '))       
        publication_date = input('Please enter the publication date in format (YYYY-MM-DD): ')
        modify_books_db.add_book(title, author_id, genre_id, isbn, publication_date)
    elif option == 2:
        user= input('Please enter library_id: ')
        book= input('Please enter the book title you would like to borrow: ').title()
        borrowed_date = datetime.today().strftime('%Y-%m-%d')
        modify_books_db.borrowed_books(user, book, borrowed_date)   
    elif option == 3:
        library_id= input('Please enter your library_id: ')
        book= input('Please enter the title of the book you are returning: ').title()
        return_date= datetime.today().strftime('%Y-%m-%d')
        modify_books_db.return_book(library_id, book, return_date)
    elif option == 4:
        book= input('Please enter the title of the book you are searching for: ').title()
        modify_books_db.search_book(book)
    elif option == 5:
        modify_books_db.display_books()
    else:
            raise ValueError("Invalid option. (1-5)")         

def author_operations():
    try:
        print("\nAuthor Operations\n1. Add a new author\n2. View author details\n3. Display all authors\n")
        option = int(input("Please pick an option to continue: "))
        if option == 1:
            name = input('What is the name of the author?').title()
            bio= input("Please provide a biography of the author.")
            modify_authors_db.add_authors(name, bio)
        elif option == 2:
            name= input("Which author are you looking for? ").title()
            modify_authors_db.search_author(name)
        elif option == 3:
            modify_authors_db.display_authors()
        else:
            raise ValueError("Invalid option. (1-3)") 

    except Exception as e:
        print(f'Error: {e}')


def user_operations():
    try:
        print("\nUser Operations\n1. Add a new user\n2. View user details\n3. Display all users\n")
        option = int(input("Please pick an option to continue: "))
        if option == 1:
            name = input('Please enter users name: ').title()
            library_id= input('Please enter new library id: ')
            modify_users_db.add_user(name, library_id)
        elif option == 2:
            library_id = input('Please enter library id: ')
            modify_users_db.search_user(library_id)
        elif option == 3:
            modify_users_db.display_users()
        else:
            raise ValueError("Invalid option. (1-3)")
    except Exception as e:
        print(f'Error: {e}')
    



def genre_operations():
      try:
        print("\nGenre Operations\n1. Add a new genre\n2. View genre details\n3. Display all genres\n")
        option = int(input("Please pick an option to continue: "))
        if option == 1:
            name= input('Please enter the Genre name: ').title()
            description= input('Please enter a description of this genre: ')
            modify_genres_db.add_genre(name, description)
        elif option == 2:
            name= input('Which genre are you looking for? ').title()
            modify_genres_db.search_genre(name)
        elif option == 3:
            modify_genres_db.display_genres()
        else:
            raise ValueError("Invalid option. (1-3)")
      except Exception as e:
          print(f'Error: {e}')