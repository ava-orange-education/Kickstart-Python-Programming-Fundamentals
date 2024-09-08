class Book: 
    def __init__(self, author, title): 
        self.author = author 
        self.title = title 
    def description(self): 
        return f"{self.title} by {self.author}" 

# Test the code 
my_book = Book("George Orwell", "1984") 
print(my_book.description()) # Outputs: 1984 by George Orwell 