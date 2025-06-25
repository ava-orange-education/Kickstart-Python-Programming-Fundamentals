def identify_odd_even(num): 
    # This function determines whether a number is odd or even. 
    # num: The number to check. 
    # Use the modulo operator to check if the number is divisible by 2 without a remainder. 
    if num % 2 == 0: 
        print(f"{num} is Even.") # If true, the number is even. 
    else:
        print(f"{num} is Odd.") # If false, the number is odd. 
# Testing the function with an even number. 
identify_odd_even(10) # Outputs: "10 is Even." 
# Testing the function with an odd number. 
identify_odd_even(7) # Outputs: "7 is Odd."
