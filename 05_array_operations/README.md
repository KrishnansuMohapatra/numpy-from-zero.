# NumPy — Array Operations

## What you'll learn

NumPy allows you to perform fast mathematical and arithmetic operations directly on arrays without writing loops.

### Element-wise Arithmetic

When two arrays have compatible shapes, standard operators apply element-by-element:

```python
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

a + b
a - b
a * b
a / b
a ** 2
```

### Universal Functions

NumPy provides fast built-in mathematical functions:

| Function | Description |
|---|---|
| `np.sqrt(arr)` | Square root |
| `np.exp(arr)` | Exponential |
| `np.log(arr)` | Natural logarithm |
| `np.abs(arr)` | Absolute value |
| `np.round(arr, decimals)` | Rounding |

### Matrix Multiplication

- **Dot product:** `np.dot(v1, v2)`
- **Matrix multiplication:** `m1 @ m2`

## Practice

The `practice.py` file contains exercises to solve independently. The `lesson.py` file contains working examples.
