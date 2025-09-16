import csv
import os

CONTACTS_FILE = 'contacts.csv'
FIELDNAMES = ['Name', 'Phone', 'Email']

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def save_contacts(contacts):
    with open(CONTACTS_FILE, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(contacts)

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    if name == '':
        print("Name cannot be empty.")
        return
    contacts.append({'Name': name, 'Phone': phone, 'Email': email})
    print("Contact added.")

def search_contacts(contacts):
    query = input("Search by name: ").strip().lower()
    filtered = [c for c in contacts if query in c['Name'].lower()]
    if not filtered:
        print("No contacts found.")
    else:
        for i, c in enumerate(filtered, 1):
            print(f"{i}. {c['Name']}, Phone: {c['Phone']}, Email: {c['Email']}")

def update_contact(contacts):
    search_contacts(contacts)
    try:
        idx = int(input("Enter contact number to update: ")) - 1
        if idx < 0 or idx >= len(contacts):
            print("Invalid contact number.")
            return
        contact = contacts[idx]
        print(f"Updating contact {contact['Name']}:")
        name = input(f"New name [{contact['Name']}]: ").strip()
        phone = input(f"New phone [{contact['Phone']}]: ").strip()
        email = input(f"New email [{contact['Email']}]: ").strip()
        if name:
            contact['Name'] = name
        if phone:
            contact['Phone'] = phone
        if email:
            contact['Email'] = email
        print("Contact updated.")
    except ValueError:
        print("Invalid input.")

def delete_contact(contacts):
    search_contacts(contacts)
    try:
        idx = int(input("Enter contact number to delete: ")) - 1
        if idx < 0 or idx >= len(contacts):
            print("Invalid contact number.")
            return
        contact = contacts.pop(idx)
        print(f"Deleted contact: {contact['Name']}")
    except ValueError:
        print("Invalid input.")

def list_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['Name']}, Phone: {c['Phone']}, Email: {c['Email']}")

def main():
    contacts = load_contacts()
    while True:
        print("\n--- Contact Book ---")
        print("1. List contacts")
        print("2. Add new contact")
        print("3. Search contacts")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Save and Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            list_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-6.")

if __name__ == '__main__':
    main()
