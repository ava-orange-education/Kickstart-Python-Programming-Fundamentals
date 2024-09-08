import numpy as np

def vector_operations(v1, v2):
    """Perform vector operations: dot product and cross product."""
    dot_product = np.dot(v1, v2)
    cross_product = np.cross(v1, v2)
    return dot_product, cross_product

def matrix_operations(m1, m2):
    """Perform matrix operations: addition, subtraction, element-wise multiplication, and dot product."""
    addition = m1 + m2
    subtraction = m1 - m2
    elementwise_multiplication = m1 * m2
    dot_product = np.dot(m1, m2)
    return addition, subtraction, elementwise_multiplication, dot_product

def transpose_matrix(matrix):
    """Transpose a matrix."""
    return np.transpose(matrix)

def display_results(vector_results, matrix_results, transpose_result):
    """Display the results of the vector and matrix operations."""
    dot_product, cross_product = vector_results
    addition, subtraction, elementwise_multiplication, dot_product_matrix = matrix_results

    print("Vector Operations:")
    print(f"Dot Product: {dot_product}")
    print(f"Cross Product: {cross_product}")
    
    print("\nMatrix Operations:")
    print(f"Addition:\n{addition}")
    print(f"Subtraction:\n{subtraction}")
    print(f"Element-wise Multiplication:\n{elementwise_multiplication}")
    print(f"Dot Product:\n{dot_product_matrix}")
    
    print("\nMatrix Transposition:")
    print(f"Transpose:\n{transpose_result}")

def main():
    # Define vectors
    vector1 = np.array([1, 2, 3])
    vector2 = np.array([4, 5, 6])

    # Define matrices
    matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

    # Perform operations
    vector_results = vector_operations(vector1, vector2)
    matrix_results = matrix_operations(matrix1, matrix2)
    transpose_result = transpose_matrix(matrix1)

    # Display results
    display_results(vector_results, matrix_results, transpose_result)

if __name__ == "__main__":
    main()
