import sqlite3
# Connect to the database
connection = sqlite3.connect('library.db')
cursor = connection.cursor()
# Insert a new book record
cursor.execute('''
    INSERT INTO books (title, author, publication_year, genre)
    VALUES (?, ?, ?, ?)
''', ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"))
print("Record inserted successfully")
# Commit the changes and close the connection
connection.commit()
connection.close()
