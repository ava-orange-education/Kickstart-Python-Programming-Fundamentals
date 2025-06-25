import numpy as np

# Creating matrices
matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Matrix addition
matrix_addition = matrix1 + matrix2

# Matrix subtraction
matrix_subtraction = matrix1 - matrix2

# Matrix multiplication (element-wise)
matrix_multiplication_elementwise = matrix1 * matrix2

# Matrix multiplication (dot product)
matrix_multiplication_dot = np.dot(matrix1, matrix2)

# Matrix transposition
matrix_transpose = np.transpose(matrix1)

print("Matrix Addition:\n", matrix_addition)
print("Matrix Subtraction:\n", matrix_subtraction)
print("Element-wise Matrix Multiplication:\n", matrix_multiplication_elementwise)
print("Dot Product Matrix Multiplication:\n", matrix_multiplication_dot)
print("Matrix Transposition:\n", matrix_transpose)
