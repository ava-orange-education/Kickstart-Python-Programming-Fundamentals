def calculate_factorial(n): 
    # This function calculates the factorial of a given number 'n'. 
    # n: A non-negative integer whose factorial is to be calculated. 
    if n < 0: 
        return "Error: Factorial of a negative number doesn't exist." 
    elif n == 0: 
        return 1 # The factorial of 0 is defined as 1. 
    else: 
        factorial = 1 
    for i in range(1, n + 1): 
        factorial *= i # Multiply 'factorial' by each number up to 'n'. 
    return factorial 
# Testing the function with various numbers. 
print(calculate_factorial(5)) # Outputs: 120, because 5! = 5*4*3*2*1 = 120 
print(calculate_factorial(0)) # Outputs: 1, as defined by the mathematical rule 0! = 1 
print(calculate_factorial(-1)) # Outputs: "Error: Factorial of a negative number doesn't exist." 
