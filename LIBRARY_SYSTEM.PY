# library project
library = {}
def add_book():
    book=input("Enter the book title: ")
    author=input("Enter the author name: ")
    
    library[book] = author
    print("book added successfully")

def view_books(): 
    if len(library) == 0:
        print("No books in the library.")
    else:
        print("Books in the library:")
        for book in library:
            print(f"{book} by {library[book]}")
def search_book():
    book=input("Enter the book title to search: ")
    if book in library:
        print(f"{book} is available in the library, authored by {library[book]}.")
    else:
        print(f"{book} is not available in the library.")
def delete_book():
    book=input("Enter the book title to delete: ")
    if book in library:
        del library[book]
        print(f"{book} has been deleted from the library.")
    else:
        print(f"{book} is not found in the library.")
def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
main()
