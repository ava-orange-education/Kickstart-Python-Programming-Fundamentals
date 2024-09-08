from datetime import time

# Step 1: Import the datetime Module
# The datetime module is used to create and manipulate time objects

# Step 2: Create a Time Object
# Creating a time object for 14:30:00 (2:30 PM)
my_time = time(14, 30, 0)
print(f"Original Time: {my_time}")  # Output: 14:30:00

# Step 3: Access Time Components
# Accessing the hour, minute, second, and microsecond components
hour = my_time.hour
minute = my_time.minute
second = my_time.second
microsecond = my_time.microsecond

print(f"Hour: {hour}, Minute: {minute}, Second: {second}, Microsecond: {microsecond}")
# Output: Hour: 14, Minute: 30, Second: 0, Microsecond: 0

# Step 4: Modify Time Components
# Creating a new time object by modifying the hour component
new_time = my_time.replace(hour=16)
print(f"Modified Time: {new_time}")  # Output: 16:30:00

# Step 5: Format the Time
# Formatting the time into a readable string
formatted_time = my_time.strftime("%H:%M:%S")
print(f"Formatted Time: {formatted_time}")  # Output: 14:30:00

# Step 6: Display the Results
# The results have been displayed above within each step
