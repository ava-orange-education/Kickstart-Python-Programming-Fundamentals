import sqlite3
# Connect to the database (or create it if it doesn't exist)
connection = sqlite3.connect('library.db')
cursor = connection.cursor()
# Create a table for books
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        publication_year INTEGER,
        genre TEXT
    )
''')
print("Table 'books' created successfully")
# Commit and close the connection
connection.commit()
connection.close()
