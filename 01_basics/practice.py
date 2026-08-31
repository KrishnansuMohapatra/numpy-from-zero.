import numpy as np

# Basic NumPy Practice
arr = np.array([10, 20, 30, 40, 50])

# 1. Number of elements
print("Number of elements:", arr.size)

# 2. Data type
print("Data type:", arr.dtype)

# 3. First element
print("First element:", arr[0])

# 4. Last element
print("Last element:", arr[-1])

# 5. Add 10 to every element
print("After adding 10:", arr + 10)

# 6. Divide every element by 10
print("After dividing by 10:", arr / 10)

# 7. Sum
print("Sum:", arr.sum())

# 8. Mean
print("Mean:", arr.mean())
