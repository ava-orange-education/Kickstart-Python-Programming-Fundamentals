import sqlite3
# Connect to the database
connection = sqlite3.connect('library.db')
cursor = connection.cursor()
# Update the genre of a specific book
cursor.execute('''
    UPDATE books
    SET genre = ?
    WHERE title = ? AND author = ?
''', ("Classic Fiction", "To Kill a Mockingbird", "Harper Lee"))
print("Record updated successfully")
# Commit the changes and close the connection
connection.commit()
connection.close()

# Connect to the database
connection = sqlite3.connect('library.db')
cursor = connection.cursor()
# Delete a specific book record
cursor.execute('''
    DELETE FROM books
    WHERE title = ? AND author = ?
''', ("1984", "George Orwell"))
print("Record deleted successfully")
# Commit the changes and close the connection
connection.commit()
connection.close()
