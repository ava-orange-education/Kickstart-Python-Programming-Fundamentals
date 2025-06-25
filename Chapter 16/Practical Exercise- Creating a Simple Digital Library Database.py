import sqlite3
# Connect to the database (or create it if it doesn't exist)
connection = sqlite3.connect('digital_library.db')
# Create a cursor object to execute SQL commands
cursor = connection.cursor()
# Create a table for authors
cursor.execute('''
    CREATE TABLE IF NOT EXISTS authors (
        author_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
''')
# Create a table for genres
cursor.execute('''
    CREATE TABLE IF NOT EXISTS genres (
        genre_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
''')

# Create a table for books
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author_id INTEGER,
        genre_id INTEGER,
        FOREIGN KEY (author_id) REFERENCES authors(author_id),
        FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
    )
''')
print("Tables created successfully")
# Commit the changes and close the connection
connection.commit()
connection.close()
# The relationships between the tables are established using foreign keys