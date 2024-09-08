
# Prompt the user to enter a year to check if it's a leap year. 
year = int(input("Enter a year to check if it's a leap year: ")) 
# Check if the year is a leap year. A year is a leap year if it's divisible by 4 but not by 100, 
# except if it is also divisible by 400. 
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): 
    print(f"{year} is a leap year.") 
else: print(f"{year} is not a leap year.") 
