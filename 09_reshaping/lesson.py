import numpy as np

# NumPy Lesson 9: Reshaping and Dimensions

arr = np.arange(1, 13)
print("1D array:", arr)

matrix_3x4 = arr.reshape(3, 4)
print("\nReshaped to 3x4:\n", matrix_3x4)

matrix_2x6 = arr.reshape(2, 6)
print("\nReshaped to 2x6:\n", matrix_2x6)

auto_cols = arr.reshape(4, -1)
print("\nReshaped (4, -1) shape:", auto_cols.shape)

flattened = matrix_3x4.flatten()
print("\nFlattened:", flattened)

print("\nOriginal 3x4:\n", matrix_3x4)
print("Transposed 4x3:\n", matrix_3x4.T)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("\nVertical stack:\n", np.vstack((a, b)))
print("Horizontal stack:", np.hstack((a, b)))
