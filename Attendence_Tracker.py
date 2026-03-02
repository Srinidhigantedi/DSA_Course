#Attendence Trackin System
#Dictionary to store attendence
attendence = {}
def show_menu():
    print("Attendence Tracker")
    print("1. Add Attendence")
    print("2. View Attendence")
    print("3. Exit")
def add_attendence():
    name = input("Enter Student name: ")
    status = input("Enter status(Present/Absent): ")
    attendence[name] = status
    print("Attendence added successfully")
def view_attendence():
    if not attendence:
        print("No recording of attendence is found")
    else:
        print("---------Attendence Records-------")
        for name,status in attendence.items():
            print(f"{name} - {status}")

def main():
    while True:
        show_menu()
        ch = input("Enter your choice: ")
        if ch =="1":
            add_attendence()
        elif ch == "2":
            view_attendence()
        elif ch == "3":  
            print("Exiting Program")
            break
        else:
            print("Invalid Choice")
main()
