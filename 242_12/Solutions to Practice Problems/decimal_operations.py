from decimal import Decimal, getcontext

def decimal_operations():
    # Set the precision for decimal operations
    getcontext().prec = 6
    
    # Create two decimal numbers
    dec1 = Decimal('1.123456')
    dec2 = Decimal('2.654321')
    
    # Perform arithmetic operations with decimals
    addition = dec1 + dec2
    subtraction = dec1 - dec2
    multiplication = dec1 * dec2
    division = dec1 / dec2
    
    # Print the results of each operation with the specified precision
    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")

# Execute the function if the script is run directly
if __name__ == "__main__":
    decimal_operations()
