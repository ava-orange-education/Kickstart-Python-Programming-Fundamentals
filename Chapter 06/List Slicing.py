# Example list 
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
# Slicing from index 2 to 5 
sub_numbers = numbers[2:6] # Outputs [2, 3, 4, 5] 
# Slicing with a step 
odd_numbers = numbers[1:10:2] # Outputs [1, 3, 5, 7, 9] 
# Omitting the start index (defaults to 0) 
first_three = numbers[:3] # Outputs [0, 1, 2] 
# Omitting the end index (goes until the end of the list) 
from_four = numbers[4:] # Outputs [4, 5, 6, 7, 8, 9] 
# Slicing with a negative step (reversing a list) 
reversed_numbers = numbers[::-1] # Outputs [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] 
