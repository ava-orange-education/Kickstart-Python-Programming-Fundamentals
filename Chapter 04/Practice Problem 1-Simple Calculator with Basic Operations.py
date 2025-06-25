# Ask the user for two numbers. These will be the operands for the arithmetic operation. 
num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: ")) 
# Ask the user to choose an arithmetic operation. The options are addition, subtraction, multiplication, and division. 
operation = input("Choose the operation (+, -, *, /): ") 
# Depending on the operation chosen by the user, perform the corresponding arithmetic operation. 
if operation == '+': 
    # If the user chooses addition, add num1 and num2, and display the result. 
    print(f"{num1} + {num2} = {num1 + num2}") 
elif operation == '-': 
    # If subtraction is chosen, subtract num2 from num1, and display the result. 
    print(f"{num1} - {num2} = {num1 - num2}") 
elif operation == '*': 
    # For multiplication, multiply num1 by num2, and display the result. 
    print(f"{num1} * {num2} = {num1 * num2}") 
elif operation == '/': 
    # Before division, check if num2 is zero to avoid division by zero error. 
    if num2 == 0: print("Error: Cannot divide by zero.") 
    else: 
        # If num2 is not zero, proceed with the division and display the result. 
        print(f"{num1} / {num2} = {num1 / num2}") 
else: 
    # If the operation entered does not match any of the expected symbols, inform the user. 
    print("Invalid operation selected.") 
