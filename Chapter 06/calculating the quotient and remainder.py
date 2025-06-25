def divmod(a, b): 
    quotient = a // b 
    remainder = a % b 
    return (quotient, remainder) # Returning a tuple 
quot, rem = divmod(10, 3) 
print("Quotient:", quot) # Outputs Quotient: 3 print("Remainder:", rem) # Outputs Remainder: 1  
