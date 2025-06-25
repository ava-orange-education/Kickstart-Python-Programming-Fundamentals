# Define the correct password. In a real application, this might be stored more securely or checked against a database. 
correct_password = "secret" 
# Initialize a counter to keep track of the number of password attempts made by the user. 
attempts = 0 
# Start a loop that allows the user up to 3 attempts to enter the correct password. 
while attempts < 3: 
    # Ask the user to input their password. 
    user_password = input("Enter password: ") 
    # Increment the counter for each attempt made. 
    attempts += 1 # Compare the entered password against the correct password. 
    if user_password == correct_password: 
        # If the password is correct, grant access and exit the loop. 
        print("Access Granted.") 
        break 
    else: 
        # If the password is incorrect, notify the user. 
        print("Wrong password.") 
    # After 3 failed attempts, lock the account and exit the loop. 
        if attempts == 3: 
            print("Account locked. Too many attempts.")
