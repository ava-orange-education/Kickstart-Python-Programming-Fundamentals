# Ask for the user's age 
age = int(input("Please enter your age: ")) 
# Determine the age group 
if age <= 12: 
    print("You are a child.") 
elif age <= 19: 
    print("You are a teenager.") 
elif age <= 64: 
    print("You are an adult.") 
else: 
    print("You are a senior.") 
