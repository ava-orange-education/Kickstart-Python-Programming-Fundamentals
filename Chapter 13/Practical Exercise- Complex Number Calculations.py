import cmath

def perform_complex_calculations():
    user_input = '3+5j'
    z = complex(user_input)
    predefined_z = 3 + 4j

    # Perform basic operations
    addition = z + predefined_z
    subtraction = z - predefined_z
    multiplication = z * predefined_z
    division = z / predefined_z

    # Use cmath module functions
    sqrt_z = cmath.sqrt(z)
    exp_z = cmath.exp(z)
    log_z = cmath.log(z)
    sin_z = cmath.sin(z)
    cos_z = cmath.cos(z)
    sinh_z = cmath.sinh(z)

    # Display results
    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")
    print(f"Square root of {z}: {sqrt_z}")
    print(f"Exponential of {z}: {exp_z}")
    print(f"Natural logarithm of {z}: {log_z}")
    print(f"Sine of {z}: {sin_z}")
    print(f"Cosine of {z}: {cos_z}")
    print(f"Hyperbolic sine of {z}: {sinh_z}")

def main():
    perform_complex_calculations()

if __name__ == "__main__":
    main()
