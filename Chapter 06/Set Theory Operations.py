fruits = {'apple', 'banana', 'cherry'} 
# Using the | operator or union() method 
tropical = {'pineapple', 'mango'} 
new_set = fruits.union(tropical) 
print(new_set) # Outputs a set containing all elements from both sets

more_fruits = {'watermelon', 'banana'}
# Using the & operator or intersection() method 
common_fruits = fruits.intersection(more_fruits) 
print(common_fruits) # Outputs a set of elements that appear in both sets

# Using the - operator or difference() method 
unique_fruits = fruits.difference(more_fruits) 
print(unique_fruits) # Outputs elements that are in fruits but not in more_fruits 



