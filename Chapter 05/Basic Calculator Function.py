# Function definitions 
def add(a, b): 
    return a + b 
def subtract(a, b): 
    return a - b 
def multiply(a, b): 
    return a * b 
def divide(a, b): 
    if b != 0: 
        return a / b 
    else: 
        return "Error: Cannot divide by zero." 
# User input 
num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: ")) 
operation = input("Choose the operation (add, subtract, multiply, divide): ") 
# Operation selection and result calculation 
if operation == "add": 
    result = add(num1, num2) 
elif operation == "subtract": 
    result = subtract(num1, num2) 
elif operation == "multiply": 
    result = multiply(num1, num2) 
elif operation == "divide": 
    result = divide(num1, num2) 
else: 
    result = "Invalid operation selected." 
# Display the result 
print(f"Result: {result}")

