from datetime import date

# Step 1: Import the datetime Module
# The datetime module is used to create and manipulate date objects

# Step 2: Create a Date Object
# Creating a date object for July 1, 2024
my_date = date(2024, 7, 1)
print(f"Original Date: {my_date}")  # Output: 2024-07-01

# Step 3: Access Date Components
# Accessing the year, month, and day components
year = my_date.year
month = my_date.month
day = my_date.day
print(f"Year: {year}, Month: {month}, Day: {day}")  # Output: Year: 2024, Month: 7, Day: 1

# Step 4: Modify Date Components
# Creating a new date object by modifying the year component
new_date = my_date.replace(year=2025)
print(f"Modified Date: {new_date}")  # Output: 2025-07-01

# Step 5: Format the Date
# Formatting the date into a readable string
formatted_date = my_date.strftime("%B %d, %Y")
print(f"Formatted Date: {formatted_date}")  # Output: July 01, 2024

# Step 6: Display the Results
# The results have been displayed above within each step
