import numpy as np

# Broadcasting example
a = np.array([1, 2, 3])
b = np.array([[10], [20], [30]])

# Add arrays using broadcasting
result = a + b
print("Array A:", a)
print("Array B:\n", b)
print("\nResult of Broadcasting (A + B):\n", result)

# Stacking arrays
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print("\nHorizontal Stack:", np.hstack((x, y)))
print("Vertical Stack:\n", np.vstack((x, y)))

# Combine random matrices
mat1 = np.random.randint(1, 10, (2, 3))
mat2 = np.random.randint(10, 20, (2, 3))

print("\nMatrix 1:\n", mat1)
print("Matrix 2:\n", mat2)

combined = np.concatenate((mat1, mat2), axis=0)
print("\nConcatenated (axis=0):\n", combined)
