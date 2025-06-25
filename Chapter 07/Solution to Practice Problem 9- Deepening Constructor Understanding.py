class Rectangle:
    def __init__(self, length=1, breadth=1):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

default_rectangle = Rectangle()
print(f"Default Area: {default_rectangle.area()}")  # Outputs: Default Area: 1
print(f"Default Perimeter: {default_rectangle.perimeter()}")  # Outputs: Default Perimeter: 4