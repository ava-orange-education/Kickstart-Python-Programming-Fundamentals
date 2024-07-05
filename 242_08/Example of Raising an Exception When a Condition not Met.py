import math

def calculate_square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(number)

def main():
    try:
        num = float(input("Enter a number to find the square root: "))
        result = calculate_square_root(num)
        print(f"The square root of {num} is {result:.2f}")
    except ValueError as error:
        print(error)

if __name__ == "__main__":
    main()
