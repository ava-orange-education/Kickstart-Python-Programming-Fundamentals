class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
    def update_name(self, new_name): 
        self.name = new_name 
    def update_age(self, new_age): 
        self.age = new_age 
    def display_info(self): 
        return f"{self.name}, {self.age} years old" 

# Test the code 
person = Person("John Doe", 30) 
print(person.display_info()) # Outputs: John Doe, 30 years old 

person.update_name("Jane Doe") 
person.update_age(31) 
print(person.display_info()) # Outputs: Jane Doe, 31 years old