def divide_numbers(dividend, divisor):
    try:
        result = dividend / divisor
        print(f"The result of dividing {dividend} by {divisor} is: {result:.2f}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    try:
        num1 = float(input("Enter the dividend: "))
        num2 = float(input("Enter the divisor: "))
        divide_numbers(num1, num2)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
