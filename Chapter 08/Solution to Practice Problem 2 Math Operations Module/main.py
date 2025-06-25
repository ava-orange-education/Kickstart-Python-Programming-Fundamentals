# Import the simple_math module 
import simple_math 
# Test the arithmetic functions 
# Addition of 15 and 23 
result_add = simple_math.add(15, 23) 
print(f"The sum of 15 and 23 is {result_add}.") 
# Subtraction of 50 from 100 
result_subtract = simple_math.subtract(100, 50) 
print(f"100 minus 50 is {result_subtract}.") 
# Multiplication of 8 by 12 
result_multiply = simple_math.multiply(8, 12) 
print(f"8 multiplied by 12 is {result_multiply}.") 
# Division of 20 by 5 
result_divide = simple_math.divide(20, 5) 
print(f"20 divided by 5 is {result_divide}.") 
# Attempt to divide by zero 
result_divide_zero = simple_math.divide(10, 0) 
print(f"Result of dividing 10 by 0 is {result_divide_zero}.") 