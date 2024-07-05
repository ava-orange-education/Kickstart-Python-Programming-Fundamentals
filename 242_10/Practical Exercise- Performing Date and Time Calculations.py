from datetime import date, timedelta

# Step 1: Import the datetime Module
# The datetime module is used to create and manipulate date objects

# Step 2: Create Date Objects
# Creating date objects for specific dates
start_date = date(2024, 7, 1)
end_date = date(2024, 7, 15)
print(f"Start Date: {start_date}")  # Output: 2024-07-01
print(f"End Date: {end_date}")      # Output: 2024-07-15

# Step 3: Add and Subtract Dates
# Adding 10 days to the start date
future_date = start_date + timedelta(days=10)
print(f"Future Date: {future_date}")  # Output: 2024-07-11

# Subtracting 10 days from the start date
past_date = start_date - timedelta(days=10)
print(f"Past Date: {past_date}")      # Output: 2024-06-21

# Step 4: Calculate Differences Between Dates
# Calculating the difference between two dates
date_difference = end_date - start_date
print(f"Difference: {date_difference}")  # Output: 14 days, 0:00:00
print(f"Difference in days: {date_difference.days}")  # Output: 14

# Step 5: Display the Results
# The results have been displayed above within each step
