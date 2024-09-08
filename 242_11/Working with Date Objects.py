from datetime import date

# Creating a date object for July 1, 2024
my_date = date(2024, 7, 1)
print(my_date)  # Output: 2024-07-01

# Accessing components of the date object
year = my_date.year
month = my_date.month
day = my_date.day

print(f"Year: {year}, Month: {month}, Day: {day}")  # Output: Year: 2024, Month: 7, Day: 1

# Modifying the date by creating a new date object
new_date = my_date.replace(year=2025)
print(new_date)  # Output: 2025-07-01

# Formatting a date object into a string
formatted_date = my_date.strftime("%B %d, %Y")
print(formatted_date)  # Output: July 01, 2024

from datetime import datetime

# Parsing a string into a date object
date_string = "July 01, 2024"
parsed_date = datetime.strptime(date_string, "%B %d, %Y").date()
print(parsed_date)  # Output: 2024-07-01
