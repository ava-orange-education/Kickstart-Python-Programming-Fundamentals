fruits = ['apple', 'banana', 'cherry'] 
fruits.append('date') 
# Now fruits = ['apple', 'banana', 'cherry', 'date'] 
fruits.insert(1, 'blueberry') 
# Now fruits = ['apple', 'blueberry', 'banana', 'cherry', 'date'] 
more_fruits = ['elderberry', 'fig'] 
fruits.extend(more_fruits) 
# Now fruits = ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry', 'fig'] 


fruits.remove('banana') 
# Now fruits = ['apple', 'blueberry', 'cherry', 'date', 'elderberry', 'fig'] 
last_fruit = fruits.pop() # Removes and returns 'fig' 
# Now fruits = ['apple', 'blueberry', 'cherry', 'date', 'elderberry'] 
fruits.clear() 
# Now fruits = [] 

fruits = ['apple', 'banana', 'cherry'] 
fruits[1] = 'blackberry' 
# Now fruits = ['apple', 'blackberry', 'cherry'] 

fruits.sort() # Sorts the list alphabetically; for numbers, it sorts them numerically 
fruits.reverse() 
# Now fruits = ['cherry', 'blackberry', 'apple'] 
count = fruits.count('apple') # count will be 1 