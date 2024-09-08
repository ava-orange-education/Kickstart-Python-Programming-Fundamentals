# List comprehension for squares of numbers 1 through 10 
squares = [x**2 for x in range(1, 11)] 
odd_squares = [x for x in squares if x % 2 != 0] 
print("Squares:", squares) 
print("Odd Squares:", odd_squares)