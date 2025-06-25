# Script to display current date and time details using datetime module
from datetime import datetime

current_time = datetime.now()  # Get the current datetime

print(f"Current Year: {current_time.year}")  # Display the current year
print(f"Current Month: {current_time.strftime('%B')}")  # Display the name of the current month
print(f"Current Week Number: {current_time.strftime('%U')}")  # Display the current week number