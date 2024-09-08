from contact_manager.add_contact import add_contact
from contact_manager.display_contacts import display_contacts
def main():
    contacts = {}
    while True:
        print("\n1. Add Contact\n2. Display Contacts\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            contacts = add_contact(contacts, name, phone)
            print("Contact added!")
        elif choice == '2':
            display_contacts(contacts)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main() 
