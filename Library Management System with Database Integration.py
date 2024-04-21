import UI

while True:
    print("\nWelcome to the Library Management System!\n\nMain Menu:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Genre Operations\n5. Quit\n")
    try:
        choice = int(input("Please pick an option to continue: "))             
        if choice == 1:
            UI.book_operations()
        elif choice == 2:
            UI.user_operations()
        elif choice == 3:
            UI.author_operations()
        elif choice == 4:
            UI.genre_operations()
        elif choice == 5:
            print("You are now exiting the Library Management System...")
            break
        else:
            raise ValueError("Invalid option. (1-5)") 
    except Exception as e:
        print(e)
