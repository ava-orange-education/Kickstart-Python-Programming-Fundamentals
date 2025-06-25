# Creating a simple tuple 
my_tuple = (1, 2, 3) 

# Tuple packing 
another_tuple = 'apple', 'banana', 'cherry' 

# Creating a single element tuple 
single_tuple = (4,) # The comma is required 

# Creating a tuple from a list 
list_to_tuple = tuple([5, 6, 7]) 
# Creating a tuple from a string 
string_to_tuple = tuple("hello") 

# Accessing the second element of the tuple 
item = another_tuple[1] 
print(item) # Outputs 'banana' 

# Accessing the last element of the tuple 
last_item = another_tuple[-1] 
print(last_item) # Outputs 'cherry' 

# Slicing the tuple to get the first two elements 
first_two = my_tuple[:2] 
print(first_two) # Outputs (1, 2) 

date_tuple = (2022, 9, 25) 
year = date_tuple[0] 
day = date_tuple[2] 
print("Year:", year) # Outputs Year: 2022 print("Day:", day) # Outputs Day: 25 
