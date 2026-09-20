import numpy as np

# NumPy Lesson 4: Indexing and Slicing

# 1. 1D Array Indexing
numbers = np.array([10, 20, 30, 40, 50, 60])
print("Original 1D array:", numbers)
print("First element (index 0):", numbers[0])
print("Third element (index 2):", numbers[2])
print("Last element (index -1):", numbers[-1])

# 2. 1D Array Slicing [start:stop:step]
print("\n1D Slicing:")
print("First three elements [0:3]:", numbers[0:3])
print("From index 2 to end [2:]:", numbers[2:])
print("Every other element [::2]:", numbers[::2])
print("Reversed array [::-1]:", numbers[::-1])

# 3. 2D Array Indexing [row, column]
matrix = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])
print("\n2D Matrix:")
print(matrix)

print("Element at row 0, col 2:", matrix[0, 2])
print("Element at row 1, col 3:", matrix[1, 3])
print("Element at row 2, col 1:", matrix[2, 1])

# 4. 2D Array Slicing
print("\n2D Slicing:")
print("Entire first row [0, :]:", matrix[0, :])
print("Entire second column [:, 1]:", matrix[:, 1])
print("Sub-matrix (first 2 rows, first 2 cols):\n", matrix[0:2, 0:2])

# 5. Modifying values via indexing
matrix[0, 0] = 999
print("\nMatrix after updating [0, 0] to 999:")
print(matrix)
