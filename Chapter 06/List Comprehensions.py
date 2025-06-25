# List of squares of numbers from 0 to 9 
squares = [x**2 for x in range(10)] 
# Creating a list of lowercase strings 
fruits = ["Apple", "Banana", "Cherry"] 
lowercase_fruits = [fruit.lower() for fruit in fruits]  

# List of even numbers from 0 to 9 
evens = [x for x in range(10) if x % 2 == 0] 
# List of fruits with more than 5 letters 
long_fruits = [fruit for fruit in fruits if len(fruit) > 5] 

# Flattening a nested list 
nested_list = [[1, 2], [3, 4], [5, 6]] 
flat_list = [item for sublist in nested_list for item in sublist] 
