import numpy as np

# Create two 3x3 matrices
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# Matrix addition
sum_matrix = A + B
print("Matrix Addition:\n", sum_matrix)

# Matrix multiplication
product_matrix = np.dot(A, B)
print("\nMatrix Multiplication:\n", product_matrix)

# Transpose of a matrix
transpose_A = A.T
print("\nTranspose of A:\n", transpose_A)
