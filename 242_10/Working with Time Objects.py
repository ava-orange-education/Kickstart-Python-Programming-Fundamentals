from datetime import time

# Creating a time object for 14:30:00 (2:30 PM)
my_time = time(14, 30, 0)
print(my_time)  # Output: 14:30:00


# Accessing components of the time object
hour = my_time.hour
minute = my_time.minute
second = my_time.second
microsecond = my_time.microsecond

print(f"Hour: {hour}, Minute: {minute}, Second: {second}, Microsecond: {microsecond}")
# Output: Hour: 14, Minute: 30, Second: 0, Microsecond: 0

# Modifying the time by creating a new time object
new_time = my_time.replace(hour=16)
print(new_time)  # Output: 16:30:00

# Formatting a time object into a string
formatted_time = my_time.strftime("%H:%M:%S")
print(formatted_time)  # Output: 14:30:00

from datetime import datetime

# Parsing a string into a time object
time_string = "14:30:00"
parsed_time = datetime.strptime(time_string, "%H:%M:%S").time()
print(parsed_time)  # Output: 14:30:00
