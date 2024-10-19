from pymongo import MongoClient
# Connect to the MongoDB server
client = MongoClient('localhost', 27017)
# Access the 'library' database (it will be created if it doesn't exist)
db = client['library']
books_collection = db['books']
# Find a book by title
book = books_collection.find_one({"title": "To Kill a Mockingbird"})
print(book)
# Find all books by a specific author
books_by_author = books_collection.find({"author": "Harper Lee"})
for book in books_by_author:
    print(book)
