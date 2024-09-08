def fibonacci(n): 
    # Generates the Fibonacci sequence up to the 'n'th number. 
    # n: The length of the Fibonacci sequence to generate. 
    if n <= 0: 
        return [] # If 'n' is 0 or negative, return an empty list. 
    elif n == 1: 
        return [0] # The sequence up to the first number is [0].
    sequence = [0, 1] 
    while len(sequence) < n: 
        # Append the sum of the last two numbers in the sequence to itself. 
        sequence.append(sequence[-1] + sequence[-2]) 
    return sequence 
# Generating the first 5 numbers of the Fibonacci sequence. 
print(fibonacci(5)) # Outputs [0, 1, 1, 2, 3] 
# Generating the Fibonacci sequence with 'n' as 1. 
print(fibonacci(1)) # Outputs [0]
