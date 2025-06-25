# Get the range within which the multiplication tables are to be printed and the number to skip. 
n = int(input("Enter the range of numbers: ")) 
skip = int(input("Enter the number to skip: ")) 
# Start the outer loop to iterate through each number in the range for creating their multiplication tables. 
for base in range(1, n + 1): 
    # If the current number is the one to skip, use continue to skip its multiplication table. 
    if base == skip: 
        continue 
    print(f"Multiplication table for {base}:") 
    # Inner loop to go through each multiplier from 1 to 10 for the current base number. 
    for multiplier in range(1, 11): 
        # Print the product of the current base number and the multiplier. 
        print(f"{base} x {multiplier} = {base * multiplier}") 
        # Print a newline after each table for better readability. 
        print("") 
