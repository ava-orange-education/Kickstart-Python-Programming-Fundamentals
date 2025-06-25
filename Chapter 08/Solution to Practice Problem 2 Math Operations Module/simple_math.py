def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the subtraction of b from a."""
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """Returns the division of a by b, handling division by zero."""
    if b == 0:
        return "Error: Division by zero"
    else:
        return a / b