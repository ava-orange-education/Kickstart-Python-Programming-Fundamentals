import sqlite3
# Connect to the database
connection = sqlite3.connect('library.db')
cursor = connection.cursor()
# Insert multiple book records
books = [
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction"),
    ("Moby Dick", "Herman Melville", 1851, "Adventure")
]
cursor.executemany('''
    INSERT INTO books (title, author, publication_year, genre)
    VALUES (?, ?, ?, ?)
''', books)
print("Multiple records inserted successfully")
# Commit the changes and close the connection
connection.commit()
connection.close()
