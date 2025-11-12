import numpy as np

# Generate a random dataset of 20 numbers
data = np.random.randint(1, 100, size=20)
print("Data:", data)

# Calculate basic statistics
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
variance = np.var(data)

print("\nMean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
print("Variance:", variance)

# Sort and find min/max
print("\nSorted Data:", np.sort(data))
print("Min Value:", np.min(data))
print("Max Value:", np.max(data))
