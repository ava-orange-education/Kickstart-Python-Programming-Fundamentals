# Creating a simple dictionary 
my_dict = {'name': 'John', 'age': 30, 'job': 'Developer'} 

# Creating a dictionary from keyword arguments 
another_dict = dict(name="Alice", age=25, job="Designer") 
# Creating a dictionary from pairs 
pair_dict = dict([('name', 'Bob'), ('age', 20)]) 

# Accessing the name from the dictionary 
print(my_dict['name']) # Outputs 'John' 

# Using get to avoid errors 
print(my_dict.get('age', 'Not Specified')) # Outputs 30 

my_dict.update({'age': 31, 'city': 'New York'}) 
print(my_dict) # Outputs {'name': 'John', 'age': 31, 'job': 'Developer', 'city': 'New York'} 


