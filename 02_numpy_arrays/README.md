# 02 — NumPy Arrays

## Notes

A NumPy array is a numerical data structure created with `np.array()`.

### What I learned

- Create a NumPy array from a Python list.
- Create a 2D array.
- Store numerical data in arrays.
- Perform element-wise arithmetic operations.

### Basic examples

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

### Array arithmetic

NumPy applies arithmetic operations element by element:

```python
numbers + 10
numbers - 10
numbers * 2
numbers / 2
```

For example:

```text
[10, 20, 30] * 2
       ↓
[20, 40, 60]
```

## Practice

The `practice.py` file contains the problems I solved for this lesson.

## Key idea

**Python list → NumPy array → numerical operations**
