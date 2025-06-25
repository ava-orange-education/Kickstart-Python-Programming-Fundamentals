# Define the tuple of days 
days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') 
# Function to check the day type 
def check_day(day): 
    if day in days_of_week[5:]: 
        print("It's a weekend!") 
    elif day in days_of_week[:5]: 
        print("It's a weekday") 
    else: 
        print("Please enter a valid day of the week.") 
# Test the function 
check_day('Saturday') 
check_day('Monday')