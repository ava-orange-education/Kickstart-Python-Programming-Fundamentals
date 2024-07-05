def perform_operation(num1, num2, operation):
    try:
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2
        else:
            raise ValueError("Invalid operation selected.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError as ve:
        print(f"Error: {ve}")
    else:
        print(f"The result of {operation} is: {result}")
    finally:
        print("Operation completed.")

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").lower()
    perform_operation(num1, num2, operation)

if __name__ == "__main__":
    main()
