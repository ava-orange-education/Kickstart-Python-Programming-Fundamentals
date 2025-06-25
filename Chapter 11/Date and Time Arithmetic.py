from datetime import date, timedelta

# Creating a date object for July 1, 2024
my_date = date(2024, 7, 1)

# Adding 10 days to the date
future_date = my_date + timedelta(days=10)
print(f"Future Date: {future_date}")  # Output: 2024-07-11


# Subtracting 10 days from the date
past_date = my_date - timedelta(days=10)
print(f"Past Date: {past_date}")  # Output: 2024-06-21


# Creating another date object for July 15, 2024
another_date = date(2024, 7, 15)
# Calculating the difference between the two dates
difference = another_date - my_date
print(f"Difference: {difference}")  # Output: 14 days, 0:00:00
print(f"Difference in days: {difference.days}")  # Output: 14


# Creating a timedelta object representing 10 days
ten_days = timedelta(days=10)
print(f"Timedelta: {ten_days}")  # Output: 10 days, 0:00:00


# Adding a timedelta to a date
future_date = my_date + ten_days
print(f"Future Date: {future_date}")  # Output: 2024-07-11

# Subtracting a timedelta from a date
past_date = my_date - ten_days
print(f"Past Date: {past_date}")  # Output: 2024-06-21
