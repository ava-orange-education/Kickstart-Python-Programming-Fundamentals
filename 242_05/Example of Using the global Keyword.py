counter = 0 # Global variable 
def increment_counter(): 
    global counter 
    counter += 1 # Modifies the global variable instead of creating a local one 
increment_counter() 
print(counter) # Prints "1" 
