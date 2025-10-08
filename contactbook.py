import csv
import os
import re

CONTACTS_FILE = 'contacts.csv'
FIELDNAMES = ['Name', 'Phone', 'Email', 'Group', 'Notes']

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

def validate_contact(name, phone, email):
    if not name:
        print("Name cannot be empty.")
        return False
    if not re.match(r"^\d{10}$", phone):
        print("Phone must be 10 digits.")
        return False
    if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Invalid email format.")
        return False
    return True

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    group = input("Enter group (Family, Friends, Work, etc.): ").strip()
    notes = input("Notes (optional): ").strip()
    if not validate_contact(name, phone, email):
        return
    contacts.append({'Name': name, 'Phone': phone, 'Email': email, 'Group': group, 'Notes': notes})
    print("Contact added.")

def list_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    sorted_contacts = sorted(contacts, key=lambda c: c['Name'])
    for i, c in enumerate(sorted_contacts, 1):
        print(f"{i}. {c['Name']}, Phone: {c['Phone']}, Email: {c['Email']}, Group: {c['Group']}, Notes: {c['Notes']}")

def import_contacts(contacts):
    file_path = input("Import from file: ").strip()
    if not os.path.exists(file_path):
        print("File not found.")
        return
    with open(file_path, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        imported = list(reader)
        contacts.extend(imported)
    print(f"Imported {len(imported)} contacts.")

def export_contacts(contacts):
    file_path = input("Export to file: ").strip()
    with open(file_path, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(contacts)
    print(f"Exported {len(contacts)} contacts.")

def main():
    contacts = load_contacts()
    while True:
        print("\n--- Contact Book ---")
        print("1. List contacts")
        print("2. Add new contact")
        print("3. Import contacts")
        print("4. Export contacts")
        print("5. Save and Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            list_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            import_contacts(contacts)
        elif choice == '4':
            export_contacts(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == '__main__':
    main()
