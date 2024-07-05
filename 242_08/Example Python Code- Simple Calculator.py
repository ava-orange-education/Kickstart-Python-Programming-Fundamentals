def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Intentional mistake: division by zero is not handled
    return a / b

def main():
    print("Simple Calculator!")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    operation = input("Choose the operation (+, -, *, /): ")

    if operation == '+':
        result = add(a, b)
    elif operation == '-':
        result = subtract(a, b)
    elif operation == '*':
        result = multiply(a, b)
    elif operation == '/':
        result = divide(a, b)
    else:
        print("Invalid operation!")
        return

    print("The result is:", result)

if __name__ == '__main__':
    main()
