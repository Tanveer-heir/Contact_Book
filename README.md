# Contact Book (Python, Tkinter GUI)

A desktop contact management application built with Python and Tkinter.  
Easily add, edit, search, import/export, and view contact details.  
Includes birthday reminders on startup!

---

## Features

- **Add, edit, delete contacts** through graphical forms
- **Display contacts** in a searchable, sortable listbox
- **Search/filter** by name, group, email, or birthday
- **Import/export contacts** to CSV files (great for backup or sharing)
- **Group contacts** by category (e.g., Family, Friends, Work) for organization
- **Birthday field and reminders**: View popup reminders for today’s birthdays
- **Full contact details** in a popup window
- **Notes field** for extra info about each contact

---

## How to Run

1. **Requirements:**  
   - Python 3.7 or higher
   - No external dependencies (Tkinter and CSV are part of Python standard library)

2. **Usage:**  
   - Download `contact_book.py` to your machine
   - Double click to run, or start from console:  
     ```
     python contact_book.py
     ```

3. **File Storage:**  
   - Contacts are saved to `contacts.csv` in the same directory

---

## CSV Format

Contacts are saved with these fields:

| Name   | Phone   | Email | Group | Birthday | Notes |
|--------|---------|-------|-------|----------|-------|

Birthday accepts formats: `YYYY-MM-DD`, `DD-MM-YYYY`, or `MM-DD`.

---

## Birthday Reminders

When you run the app, it checks who has a birthday today and pops up a notification for those contacts.

---

## Import/Export

- Export: Save all contacts to a user-named CSV file.
- Import: Add contacts from any CSV file with the expected columns.

---

## Example Usage

- Add and save a new contact with birthday:
- Search all contacts in "Friends" group
- View today's birthdays in popup

---

## License

This project is provided under the MIT License.  
See the LICENSE file for details.

---

## Author

Created by Tanveer Singh  
If you have suggestions or want to contribute, submit a pull request or contact!

---

## Contributions

All contributions, feature suggestions, and bug reports are welcome!

