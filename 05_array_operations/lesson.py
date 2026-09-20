import numpy as np

# NumPy Lesson 5: Array Operations

a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

print("Array A:", a)
print("Array B:", b)
print("A + B:", a + b)
print("A - B:", a - b)
print("A * B:", a * b)
print("A / B:", a / b)
print("A ** 2:", a ** 2)

values = np.array([1, 4, 9, 16, 25])
print("\nValues:", values)
print("Square root:", np.sqrt(values))
print("Exponential:", np.exp(np.array([1, 2, 3])))
print("Natural Log:", np.log(np.array([1, np.e, 10])))
print("Absolute values:", np.abs(np.array([-5, 10, -20, 30])))

floats = np.array([3.14159, 2.71828, 1.41421])
print("\nFloating point values:", floats)
print("Rounded to 2 decimals:", np.round(floats, 2))

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print("\nDot product:", np.dot(v1, v2))

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
print("Matrix multiplication:\n", m1 @ m2)
