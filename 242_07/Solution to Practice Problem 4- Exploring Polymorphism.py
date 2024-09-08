class Animal: 
    def speak(self): 
        pass 

class Dog(Animal): 
    def speak(self): 
        return "Bark!" 

class Cat(Animal): 
    def speak(self): 
        return "Meow!" 

class Bird(Animal): 
    def speak(self): 
        return "Tweet!" 
    
# Test the code 
animals = [Dog(), Cat(), Bird()] 
for animal in animals: 
    print(animal.speak())