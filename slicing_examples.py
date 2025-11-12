import numpy as np

# Create a 2D array
arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print("Original Array:\n", arr)

# Slicing examples
print("\nFirst row:", arr[0])
print("Second column:", arr[:, 1])
print("Subarray (first 2 rows, first 3 columns):\n", arr[:2, :3])

# Modify a slice
arr[0, 0] = 999
print("\nModified Array:\n", arr)

# Boolean indexing example
print("\nElements > 60:\n", arr[arr > 60])
