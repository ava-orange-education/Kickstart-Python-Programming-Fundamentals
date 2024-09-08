def is_prime(number): 
    # Checks if a number is prime. 
    # A prime number is only divisible by 1 and itself, and must be greater than 1. 
    if number <= 1: 
        return False 
    # Numbers less than or equal to 1 are not prime. 
    for i in range(2, int(number**0.5) + 1): 
        # Loop from 2 to the square root of number, checking for factors. 
        if number % i == 0: 
            return False # If a factor is found, number is not prime. 
        return True # If no factors are found, number is prime. 
# Testing the function with a prime number. 
print(is_prime(11)) # Outputs True, indicating 11 is a prime number. 
# Testing the function with a non-prime number. 
print(is_prime(4)) # Outputs False, indicating 4 is not a prime number. 
