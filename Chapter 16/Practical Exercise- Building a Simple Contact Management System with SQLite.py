import sqlite3
# Connect to the database
connection = sqlite3.connect('contacts.db')
cursor = connection.cursor()
# Create a table for contacts
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        contact_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT
    )
''')
print("Table 'contacts' created successfully")
# Commit the changes and close the connection
connection.commit()
connection.close()
connection = sqlite3.connect('contacts.db')
cursor = connection.cursor()

# Insert sample contacts
contacts = [
    ("Alice Smith", "123-456-7890", "alice@example.com"),
    ("Bob Johnson", "987-654-3210", "bob@example.com"),
    ("Charlie Brown", "555-555-5555", "charlie@example.com")
]
cursor.executemany('''
    INSERT INTO contacts (name, phone, email)
    VALUES (?, ?, ?)
''', contacts)
print("Sample contacts inserted successfully")
connection.commit()
connection.close()
connection = sqlite3.connect('contacts.db')
cursor = connection.cursor()
# Retrieve all contacts
cursor.execute('SELECT * FROM contacts')
all_contacts = cursor.fetchall()
# Display the contacts
print("Contact List:")
for contact in all_contacts:
    print(f"ID: {contact[0]}, Name: {contact[1]}, Phone: {contact[2]}, Email: {contact[3]}")
connection.close()
connection = sqlite3.connect('contacts.db')
cursor = connection.cursor()
# Update a contact's phone number
cursor.execute('''
    UPDATE contacts
    SET phone = ?
    WHERE name = ?
''', ("111-222-3333", "Alice Smith"))
print("Contact updated successfully")
connection.commit()
connection.close()
connection = sqlite3.connect('contacts.db')
cursor = connection.cursor()
# Delete a contact
cursor.execute('''
    DELETE FROM contacts
    WHERE name = ?
''', ("Charlie Brown",))
print("Contact deleted successfully")
connection.commit()
connection.close()
