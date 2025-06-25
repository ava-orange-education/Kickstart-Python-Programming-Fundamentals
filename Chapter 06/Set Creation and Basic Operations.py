# Creating a set with curly braces 
fruits = {'apple', 'banana', 'cherry'} 
# Creating a set from a list using set() 
more_fruits = set(['orange', 'melon', 'banana']) 

fruits.add('date') 
print(fruits) # Outputs something like {'banana', 'date', 'apple', 'cherry'}

fruits.remove('banana') 
print(fruits) # Outputs something like {'date', 'apple', 'cherry'}

fruits.discard('banana') # Does nothing if 'banana' is not in the set 

