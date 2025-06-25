from datetime import datetime

# Creating a datetime object for July 1, 2024, 14:30:00
my_datetime = datetime(2024, 7, 1, 14, 30, 0)
print(my_datetime)  # Output: 2024-07-01 14:30:00


# Accessing components of the datetime object
year = my_datetime.year
month = my_datetime.month
day = my_datetime.day
hour = my_datetime.hour
minute = my_datetime.minute
second = my_datetime.second

print(f"Year: {year}, Month: {month}, Day: {day}, Hour: {hour}, Minute: {minute}, Second: {second}")
# Output: Year: 2024, Month: 7, Day: 1, Hour: 14, Minute: 30, Second: 0


# Modifying the datetime by creating a new datetime object
new_datetime = my_datetime.replace(year=2025)
print(new_datetime)  # Output: 2025-07-01 14:30:00



# Formatting a datetime object into a string
formatted_datetime = my_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)  # Output: 2024-07-01 14:30:00


# Parsing a string into a datetime object
date_string = "2024-07-01 14:30:00"
parsed_datetime = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(parsed_datetime)  # Output: 2024-07-01 14:30:00
