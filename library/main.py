from library import add_book, view_books, remove_book

while True:
    print("\n1. Add Book")
    print("2. View Books")
    print("3. Remove Book")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Book name: ")
        add_book(title)

    elif choice == "2":
        view_books()

    elif choice == "3":
        title = input("Book name: ")
        remove_book(title)

    elif choice == "4":
        break

    else:
        print("Invalid choice")