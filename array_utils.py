import numpy as np

# Create a 1D array
arr = np.array([10, 20, 30, 40, 50])

print("Original Array:", arr)

# Basic operations
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))
print("Sum:", np.sum(arr))

# Reshaping example
reshaped = arr.reshape(5, 1)
print("\nReshaped Array (5x1):\n", reshaped)

# Random array example
random_arr = np.random.randint(1, 100, size=(3, 3))
print("\nRandom 3x3 Array:\n", random_arr)
