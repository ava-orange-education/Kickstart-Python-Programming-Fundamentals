import numpy as np

def basic_matrix_operations():
    # Create two matrices
    matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    
    # Perform matrix addition
    addition = matrix1 + matrix2
    print(f"Matrix Addition:\n{addition}")
    
    # Perform matrix subtraction
    subtraction = matrix1 - matrix2
    print(f"Matrix Subtraction:\n{subtraction}")
    
    # Perform element-wise multiplication of the matrices
    elementwise_multiplication = matrix1 * matrix2
    print(f"Element-wise Multiplication:\n{elementwise_multiplication}")
    
    # Perform matrix multiplication (dot product) of the matrices
    dot_product = np.dot(matrix1, matrix2)
    print(f"Dot Product Matrix Multiplication:\n{dot_product}")

# Execute the function if the script is run directly
if __name__ == "__main__":
    basic_matrix_operations()
