class Dog: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
    def speak(self, sound): 
        return f"{self.name} says {sound}" 
    def birthday(self): 
        self.age += 1 # Updates the age attribute of the same object 
        return f"Happy {self.age}th Birthday, {self.name}!" 
my_dog = Dog("Buddy", 5) 
print(my_dog.birthday()) # Outputs: Happy 6th Birthday, Buddy!  
