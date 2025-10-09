import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import csv
import os
from datetime import datetime

CONTACTS_FILE = 'contacts.csv'
FIELDNAMES = ['Name', 'Phone', 'Email', 'Group', 'Birthday', 'Notes']

def load_contacts(filename=CONTACTS_FILE):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def save_contacts(contacts, filename=CONTACTS_FILE):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(contacts)

class ContactBook(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Contact Book')
        self.geometry('700x450')
        self.contacts = load_contacts()
        self.create_widgets()
        self.update_listbox()
        self.birthday_reminder()

    def create_widgets(self):
        self.listbox = tk.Listbox(self, height=15, width=90)
        self.listbox.pack(pady=10)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text='Add', command=self.add_contact).grid(row=0, column=0)
        tk.Button(btn_frame, text='Edit', command=self.edit_contact).grid(row=0, column=1)
        tk.Button(btn_frame, text='Delete', command=self.delete_contact).grid(row=0, column=2)
        tk.Button(btn_frame, text='Search', command=self.search_contacts).grid(row=0, column=3)
        tk.Button(btn_frame, text='Export', command=self.export_contacts).grid(row=0, column=4)
        tk.Button(btn_frame, text='Import', command=self.import_contacts).grid(row=0, column=5)
        tk.Button(btn_frame, text='Details', command=self.view_details).grid(row=0, column=6)
        tk.Button(btn_frame, text='Save', command=lambda: save_contacts(self.contacts)).grid(row=0, column=7)
        
        self.status = tk.Label(self, text='', fg='blue')
        self.status.pack(pady=5)

    def update_listbox(self, filtered=None):
        self.listbox.delete(0, tk.END)
        contacts = filtered if filtered is not None else self.contacts
        for c in contacts:
            self.listbox.insert(
                tk.END,
                f"{c['Name']} | {c['Phone']} | {c['Email']} | {c['Group']} | {c.get('Birthday','')}")
        self.status['text'] = f"{len(contacts)} contact(s) loaded."

    def add_contact(self):
        data = self.prompt_contact()
        if data:
            self.contacts.append(data)
            self.update_listbox()
            self.status['text'] = "Contact added!"

    def edit_contact(self):
        idx = self.listbox.curselection()
        if not idx:
            messagebox.showerror('Error', 'Select a contact to edit.')
            return
        old_data = self.contacts[idx[0]]
        new_data = self.prompt_contact(old_data)
        if new_data:
            self.contacts[idx[0]] = new_data
            self.update_listbox()
            self.status['text'] = "Contact updated!"

    def delete_contact(self):
        idx = self.listbox.curselection()
        if not idx:
            messagebox.showerror('Error', 'Select a contact to delete.')
            return
        if messagebox.askyesno('Confirm', 'Delete contact?'):
            name = self.contacts.pop(idx[0])['Name']
            self.update_listbox()
            self.status['text'] = f"Deleted contact: {name}"

    def search_contacts(self):
        query = simpledialog.askstring('Search', 'Enter name/group/email:')
        if query:
            filtered = [
                c for c in self.contacts
                if query.lower() in c['Name'].lower()
                or query.lower() in c['Group'].lower()
                or query.lower() in c['Email'].lower()
                or query.lower() in c.get('Birthday','').lower()
            ]
            self.update_listbox(filtered)
            self.status['text'] = f"Search results for '{query}'"

    def export_contacts(self):
        fname = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[('CSV Files', '*.csv')])
        if fname:
            save_contacts(self.contacts, fname)
            self.status['text'] = f"Exported contacts to {fname}"

    def import_contacts(self):
        fname = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
        if fname:
            imported = load_contacts(fname)
            count_before = len(self.contacts)
            self.contacts.extend(imported)
            self.update_listbox()
            self.status['text'] = f"Imported {len(imported)} contacts."

    def view_details(self):
        idx = self.listbox.curselection()
        if not idx:
            messagebox.showerror('Error', 'Select a contact to view details.')
            return
        c = self.contacts[idx[0]]
        details = "\n".join(f"{field}: {c.get(field,'')}" for field in FIELDNAMES)
        messagebox.showinfo("Contact Details", details)

    def birthday_reminder(self):
        today = datetime.now().strftime('%m-%d')
        bdays = [
            c for c in self.contacts
            if c.get('Birthday','').strip() and today == self.birthday_mmdd(c['Birthday'])
        ]
        if bdays:
            msg = "Today's birthdays:\n" + "\n".join(f"{c['Name']} ({c['Birthday']})" for c in bdays)
            messagebox.showinfo("Birthday Reminder", msg)

    def birthday_mmdd(self, bdate):
        try:
            for fmt in ['%Y-%m-%d', '%d-%m-%Y', '%m-%d']:
                try:
                    dt = datetime.strptime(bdate.strip(), fmt)
                    return dt.strftime('%m-%d')
                except ValueError:
                    continue
            return ''
        except Exception:
            return ''

    def prompt_contact(self, old=None):
        name = simpledialog.askstring('Name', 'Enter name:', initialvalue=(old['Name'] if old else ''))
        phone = simpledialog.askstring('Phone', 'Enter phone number:', initialvalue=(old['Phone'] if old else ''))
        email = simpledialog.askstring('Email', 'Enter email:', initialvalue=(old['Email'] if old else ''))
        group = simpledialog.askstring('Group', 'Enter group:', initialvalue=(old['Group'] if old else ''))
        birthday = simpledialog.askstring('Birthday', 'Birthday (YYYY-MM-DD):', initialvalue=(old.get('Birthday','') if old else ''))
        notes = simpledialog.askstring('Notes', 'Notes:', initialvalue=(old.get('Notes','') if old else ''))
        if name and phone:
            return {'Name': name, 'Phone': phone, 'Email': email, 'Group': group, 'Birthday': birthday, 'Notes': notes}
        else:
            messagebox.showerror('Error', 'Name and phone required.')
            return None

if __name__ == '__main__':
    app = ContactBook()
    app.mainloop()
