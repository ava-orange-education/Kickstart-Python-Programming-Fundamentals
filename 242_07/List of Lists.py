# A simple list of lists 
matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] 
# A list of lists to represent data in a small spreadsheet 
spreadsheet = [ ["Name", "Age", "City"], ["Alice", 30, "New York"], ["Bob", 27, "Los Angeles"] ] 

# Accessing the first element of the first row in the matrix 
first_item = matrix[0][0] # Outputs 1 
# Accessing the city of the second person in the spreadsheet 
city = spreadsheet[1][2] # Outputs "New York" 

# Changing an element in the matrix 
matrix[0][0] = 10 
# Changing the age of the second person in the spreadsheet 
spreadsheet[1][1] = 31 

