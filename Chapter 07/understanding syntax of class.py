class Animal: 
    # Class attribute 
    is_living = True 
    # Method defined within the class 
    def speak(self): 
        return "This animal makes a sound" 
generic_animal = Animal() 
print(generic_animal.is_living) # Outputs: True 
print(generic_animal.speak()) # Outputs: This animal makes a sound 
