# Request the user to specify the starting and ending numbers of a range. The program will find even numbers within this range. 
start_range = int(input("Enter the start of the range: ")) 
end_range = int(input("Enter the end of the range: ")) 
# Initialize a variable to keep track of the sum of even numbers. 
sum_even = 0 
# Loop through each number in the user-defined range. 
for number in range(start_range, end_range + 1): 
    # Check if the current number is even. 
    if number % 2 == 0: 
        # If the number is even, add it to the sum_even variable. 
        sum_even += number 
        # After looping through the range, print the total sum of even numbers found.
print(f"The sum of even numbers from {start_range} to {end_range} is {sum_even}.") 
