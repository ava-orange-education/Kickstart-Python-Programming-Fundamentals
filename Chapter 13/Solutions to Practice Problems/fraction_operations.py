from fractions import Fraction

def fraction_operations():
    # Create two fractions
    frac1 = Fraction(3, 4)
    frac2 = Fraction(1, 2)
    
    # Perform arithmetic operations with fractions
    addition = frac1 + frac2
    subtraction = frac1 - frac2
    multiplication = frac1 * frac2
    division = frac1 / frac2
    
    # Print the results of each operation
    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")

# Execute the function if the script is run directly
if __name__ == "__main__":
    fraction_operations()
