from fractions import Fraction
from decimal import Decimal, getcontext

def float_arithmetic(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    return addition, subtraction, multiplication, division

def fraction_arithmetic(a, b):
    frac1 = Fraction(a)
    frac2 = Fraction(b)
    addition = frac1 + frac2
    subtraction = frac1 - frac2
    multiplication = frac1 * frac2
    division = frac1 / frac2
    return addition, subtraction, multiplication, division

def decimal_arithmetic(a, b, precision):
    getcontext().prec = precision
    dec1 = Decimal(a)
    dec2 = Decimal(b)
    addition = dec1 + dec2
    subtraction = dec1 - dec2
    multiplication = dec1 * dec2
    division = dec1 / dec2
    return addition, subtraction, multiplication, division

def display_results(float_results, fraction_results, decimal_results):
    operations = ["Addition", "Subtraction", "Multiplication", "Division"]
    print("Floating-Point Arithmetic Results:")
    for op, result in zip(operations, float_results):
        print(f"{op}: {result}")
    print("\nFraction Arithmetic Results:")
    for op, result in zip(operations, fraction_results):
        print(f"{op}: {result}")
    print("\nDecimal Arithmetic Results (with specified precision):")
    for op, result in zip(operations, decimal_results):
        print(f"{op}: {result}")

def main():
    a = 1.123456
    b = 2.654321
    precision = 6

    float_results = float_arithmetic(a, b)
    fraction_results = fraction_arithmetic(a, b)
    decimal_results = decimal_arithmetic(str(a), str(b), precision)

    display_results(float_results, fraction_results, decimal_results)

if __name__ == "__main__":
    main()
