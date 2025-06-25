# Define the Book class 
class Book: 
    # Class attribute 
    library_name = "Local Library" 
    # Initialize class without constructor 
    books = [] 
    @classmethod 
    def add_book(cls, title, author): 
        cls.books.append({'title': title, 'author': author}) 
        print(f"Book added: {title} by {author}") 
    @classmethod 
    def remove_book(cls, title): 
        for book in cls.books: 
            if book['title'] == title: 
                cls.books.remove(book) 
                print(f"Book removed: {title}") 
                return print("Book not found.") 
    @classmethod 
    def display_books(cls): 
        if cls.books: 
            print("Listing all books:") 
            for book in cls.books: 
                print(f"{book['title']} by {book['author']}") 
        else:
            print("No books in the library.") 
# Main interaction loop 
while True: 
    print("\n1. Add a book") 
    print("2. Remove a book") 
    print("3. Show all books") 
    print("4. Exit") 
    choice = input("Enter your choice: ") 
    if choice == '1': 
        title = input("Enter the title of the book: ") 
        author = input("Enter the author of the book: ") 
        Book.add_book(title, author) 
    elif choice == '2': 
        title = input("Enter the title of the book to remove: ") 
        Book.remove_book(title) 
    elif choice == '3': 
        Book.display_books() 
    elif choice == '4': 
        print("Exiting program.") 
        break 
    else: 
        print("Invalid choice. Please choose a valid option.")
