from operations import add_contact,search_contact,update_contact,delete_contact,display_contacts

while True:
    print("\nPhonebook Application")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Display Contacts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        update_contact()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        display_contacts()
    elif choice == '6':
        print("Exiting the phonebook application.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")