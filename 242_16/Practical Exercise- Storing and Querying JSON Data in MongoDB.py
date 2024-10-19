from pymongo import MongoClient
# Connect to the MongoDB server
client = MongoClient('localhost', 27017)
db = client['digital_library']
print("Connected to MongoDB successfully")
# Create a collection called 'books'
books_collection = db['books']
# Insert multiple documents into the 'books' collection
books = [
    {
        "title": "1984",
        "author": "George Orwell",
        "publication_year": 1949,
        "genres": ["Dystopian", "Science Fiction"]
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "publication_year": 1813,
        "genres": ["Romance", "Classic"]
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publication_year": 1925,
        "genres": ["Classic", "Fiction"]
    }
]
books_collection.insert_many(books)
print("Books inserted successfully")
# Find all books by George Orwell
books_by_orwell = books_collection.find({"author": "George Orwell"})
print("Books by George Orwell:")
for book in books_by_orwell:
    print(book)
# Find all books published in 1949
books_published_in_1949 = books_collection.find({"publication_year": 1949})
print("Books published in 1949:")
for book in books_published_in_1949:
    print(book)
# Find all books in the 'Classic' genre
classic_books = books_collection.find({"genres": "Classic"})
print("Classic genre books:")
for book in classic_books:
    print(book)
