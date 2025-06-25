# Prompt for user input on the range of base numbers and the multiplier limit 
start_number = int(input("Enter the start number for the multiplication tables: "))
# User-defined range start 
end_number = int(input("Enter the end number for the multiplication tables: ")) 
# User-defined range end 
max_multiplier = int(input("Enter the maximum multiplier: ")) # User-defined multiplier limit 
# Outer loop for each base number - Demonstrating hierarchical iteration through the range of base numbers 
for base in range(start_number, end_number + 1): 
    print(f"\nMultiplication table for {base}:") # Formatting output for each base number's table 
    # Nested loop for each multiplier - Managing tasks that require iterations within iterations 
    for multiplier in range(1, max_multiplier + 1): 
        print(f"{base} x {multiplier} = {base * multiplier}") # Performing multiplication and displaying results 
# Indicates the completion of all multiplication tables 
print("\nMultiplication tables complete.") 
