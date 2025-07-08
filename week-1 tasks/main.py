import os
import pyfiglet
import json
import sys

CONTACTS_FILE = "contacts.json"


def load_contacts():
    '''A method to load contacts'''
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    else:
        return []
    

def save_contacts(contacts):
    """A method to save contacts"""
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)



def add_contact():
    """A method to add contact"""
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    contact = {
        'name' : name,
        'phone' : phone,
        'email' : email
    }
    contacts = load_contacts()
    if contact not in contacts:
        contacts.append(contact)
        save_contacts(contacts)
        print(f"Contact added succesfully. ")

    else:
        print('Contact already exists')


def display():
    """A method to display contacts."""
    contacts = load_contacts()
    if not contacts:
        print("\nNo Contacts to display")
        return
    
    for contact in contacts:
        print('\n')
        for key, value in contact.items():
            print(key," : ", value)


def update_contact():
    """A method to update contacts"""
    name_to_edit = input("Enter the name of the contact to edit: ").strip()
    contacts = load_contacts()

    for contact in contacts:
        if contact['name'].lower() == name_to_edit.lower():
            print(f"\nEditing contact for {contact['name']}")
            new_name = input(f"New name (press Enter to keep '{contact['name']}'): ").strip()
            new_phone = input(f"New phone (press Enter to keep '{contact['phone']}'): ").strip()
            new_email = input(f"New email (press Enter to keep '{contact['email']}'): ").strip()

            if new_name:
                contact['name'] = new_name
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email

            save_contacts(contacts)
            print("Contact updated successfully!")
            return

    print("Contact not found.")


def search():
    """A method to search contacts by name or number"""
    contacts = load_contacts()
    if not contacts:
        print("No contacts to search.")
        return
    

    
    
    contact_to_search = str(input(f"Enter the name you want to search: "))
    for contact in contacts:
        if contact_to_search.lower() in contact['name'].lower():
            print('\n')
            for key, value in contact.items():
                print(key," : ", value)



def main():
    print(pyfiglet.figlet_format("Contact Manager"))
    print("\nOptions:")
    print("\n1.Add New Contact\n2.Update Contact\n3.Display All Contact\n4.Search By Name\n5.Exit")

    while True:
        try:
            user_input = input("\nEnter your Choice: ")
            choice = int(user_input)
        except ValueError:
            print("Invalid Input. Please enter an Interger ")
        else:
            match choice:
                case 1:
                    add_contact()
                
                case 2:
                    update_contact()

                case 3:
                    display()

                
                case 4:
                    search()

                case 5:
                    print("\nExiting...")
                    sys.exit(0)
                
                case _:
                    print("Invalid Input. Choose one of the choices.")

if __name__ == "__main__":
    main()