import numpy as np

# NumPy Lesson 3: Array Properties

# Create a 1D array
arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
print("Shape:", arr.shape)
print("Number of dimensions:", arr.ndim)
print("Number of elements:", arr.size)
print("Data type:", arr.dtype)

# Create a 2D array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n2D Array:")
print(matrix)
print("Shape:", matrix.shape)
print("Number of dimensions:", matrix.ndim)
print("Number of elements:", matrix.size)
print("Data type:", matrix.dtype)

# Create a floating-point array
temperatures = np.array([25.5, 28.2, 30.1, 27.8])

print("\nTemperature array:")
print(temperatures)
print("Shape:", temperatures.shape)
print("Dimensions:", temperatures.ndim)
print("Size:", temperatures.size)
print("Data type:", temperatures.dtype)
