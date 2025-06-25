def get_positive_number():
    num = float(input("Enter a positive number: "))
    if num <= 0:
        raise ValueError("The number is not positive. Please enter a positive number.")
    return num

try:
    positive_number = get_positive_number()
    print(f"You entered: {positive_number}")
except ValueError as error:
    print(error)
