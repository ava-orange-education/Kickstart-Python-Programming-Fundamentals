from decimal import Decimal, getcontext

# Set precision
getcontext().prec = 6

dec1 = Decimal('1.123456')
dec2 = Decimal('2.654321')

# Arithmetic operations with decimals
addition = dec1 + dec2
subtraction = dec1 - dec2
multiplication = dec1 * dec2
division = dec1 / dec2

print(f"Addition: {addition}")  # Output: 3.77778
print(f"Subtraction: {subtraction}")  # Output: -1.53087
print(f"Multiplication: {multiplication}")  # Output: 2.98408
print(f"Division: {division}")  # Output: 0.423074
