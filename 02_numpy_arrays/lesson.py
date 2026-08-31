import numpy as np

# NumPy Lesson 2: NumPy Arrays

# A NumPy array stores numerical data in a structured way.
numbers = np.array([10, 20, 30, 40, 50])
print("Array:", numbers)

# Create an array from a Python list.
prices = [100, 200, 300, 400]
price_array = np.array(prices)
print("Price array:", price_array)

# A 2D array contains rows and columns.
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("2D array:")
print(matrix)

# NumPy supports element-wise arithmetic.
sales = np.array([1000, 1500, 1200, 1800])
print("Sales:", sales)
print("Sales + 100:", sales + 100)
print("Sales - 100:", sales - 100)
print("Sales * 2:", sales * 2)
print("Sales / 2:", sales / 2)
