class Dog: 
    # Class attribute 
    species = 'Canine' 
    def __init__(self, name, age): 
        # Instance attributes 
        self.name = name 
        self.age = age 
my_dog = Dog("Buddy", 5) 
print(my_dog.species) 
# Accessing class attribute 
print(my_dog.name) # Accessing instance attribute 
