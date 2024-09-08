class Dog: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
    # A simple method to describe the dog 
    def describe(self): 
        return f"{self.name} is {self.age} years old." 
    # Another method to simulate the dog making a sound 
    def speak(self, sound): 
        return f"{self.name} says {sound}"

my_dog = Dog("Buddy", 5) 
print(my_dog.describe()) # Outputs: Buddy is 5 years old. 
print(my_dog.speak("Woof")) # Outputs: Buddy says Woof 
