class Rectangle: 
    def __init__(self, length=1, breadth=1): 
        self.length = length 
        self.breadth = breadth 
    def area(self): 
        return self.length * self.breadth 
    def perimeter(self): 
        return 2 * (self.length + self.breadth) 

# Test the code 
rectangle = Rectangle(5, 3) 
print(f"Area: {rectangle.area()}") # Outputs: Area: 15 
print(f"Perimeter: {rectangle.perimeter()}") # Outputs: Perimeter: 16