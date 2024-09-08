# Ask the user to define the range within which they want to find prime numbers. 
start = int(input("Enter the start of the range: ")) 
end = int(input("Enter the end of the range: ")) 
print(f"Prime numbers between {start} and {end} are:") 
# Loop through each number in the defined range. 
for num in range(start, end + 1): 
    # Only consider numbers greater than 1, as prime numbers are greater than 1. 
    if num > 1: 
        # Use a nested loop to try dividing the number by all smaller numbers. 
        for i in range(2, num): 
            # If the number is divisible by any number other than 1 and itself, it's not prime. 
            if (num % i) == 0: 
                break 
            else: 
                # If the loop completes without finding any factors, num is prime. 
                print(num) 

