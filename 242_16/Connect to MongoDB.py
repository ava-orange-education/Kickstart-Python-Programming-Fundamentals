from pymongo import MongoClient
# Connect to the MongoDB server
client = MongoClient('localhost', 27017)
# Access the 'library' database (it will be created if it doesn't exist)
db = client['library']
print("Connected to MongoDB successfully")
# Create a collection called 'books'
books_collection = db['books']
# Insert a document into the 'books' collection
book = {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "publication_year": 1960,
    "genres": ["Fiction", "Classic"]
}

book_id = books_collection.insert_one(book).inserted_id
print(f"Book inserted with ID: {book_id}")
