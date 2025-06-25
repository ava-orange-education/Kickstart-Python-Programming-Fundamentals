import math

def perform_calculations():
    # Prompt user for input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2
    exponentiation = math.pow(num1, num2)
    modulo = num1 % num2

    # Display results
    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")
    print(f"Exponentiation: {exponentiation}")
    print(f"Modulo: {modulo}")

def main():
    perform_calculations()

if __name__ == "__main__":
    main()
