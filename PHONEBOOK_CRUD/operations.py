phonebook = {}

def add_contact():
    name = input("Enter the name of the contact: ")
    number = input("Enter the phone number of the contact: ")

    if name in phonebook:
        print(f"Contact '{name}' already exists in the phonebook.")
    else:
        phonebook[name] = number
        print(f"Contact '{name}' has been added to the phonebook.")


def update_contact():
    name = input("Enter the name of the contact to update: ")

    if name in phonebook:
        new_number = input("Enter the new phone number: ")
        phonebook[name] = new_number
        print(f"Contact '{name}' has been updated.")
    else:
        print(f"Contact '{name}' not found in the phonebook.")


def search_contact():
    name = input("Enter the name of the contact to search: ")

    if name in phonebook:
        print(f"{name} : {phonebook[name]}")
    else:
        print(f"Contact '{name}' not found in the phonebook.")


def delete_contact():
    name = input("Enter the name of the contact to delete: ")

    if name in phonebook:
        del phonebook[name]
        print(f"Contact '{name}' has been deleted.")
    else:
        print(f"Contact '{name}' not found in the phonebook.")


def display_contacts():
    if len(phonebook) == 0:
        print("Phonebook is empty.")
    else:
        print("Phonebook Contacts:")
        for name, number in phonebook.items():
            print(name, ":", number)