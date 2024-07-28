import math

def perform_advanced_calculations():
    # Prompt user for input
    num = float(input("Enter a number: "))

    # Perform advanced calculations
    sqrt_result = math.sqrt(num)
    log_result = math.log(num)
    sin_result = math.sin(num)
    cos_result = math.cos(num)
    sinh_result = math.sinh(num)

    # Display results
    print(f"Square root of {num}: {sqrt_result}")
    print(f"Natural logarithm of {num}: {log_result}")
    print(f"Sine of {num} (in radians): {sin_result}")
    print(f"Cosine of {num} (in radians): {cos_result}")
    print(f"Hyperbolic sine of {num}: {sinh_result}")

def main():
    perform_advanced_calculations()

if __name__ == "__main__":
    main()
