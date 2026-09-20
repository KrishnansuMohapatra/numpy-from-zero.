# NumPy — Indexing & Slicing

## What you'll learn

Indexing and slicing allow you to access, extract, and modify individual elements or entire subsets of NumPy arrays.

### 1D Indexing & Slicing

1D indexing works similarly to Python lists:

```python
arr = np.array([10, 20, 30, 40, 50])

arr[0]      # 10 (first item)
arr[-1]     # 50 (last item)
arr[1:4]    # [20, 30, 40] (from index 1 up to index 4)
arr[::2]    # [10, 30, 50] (every 2nd item)
```

### 2D Indexing: `[row, column]`

Unlike Python's nested lists (`matrix[row][col]`), NumPy uses comma-separated coordinates:

```python
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

matrix[0, 1]    # 20 (row 0, column 1)
matrix[2, 2]    # 90
```

### 2D Slicing

Use the colon `:` to select entire rows or columns:

```python
matrix[0, :]     # Entire row 0 -> [10, 20, 30]
matrix[:, 1]     # Entire column 1 -> [20, 50, 80]
matrix[0:2, 1:3] # Sub-matrix (rows 0-1, cols 1-2)
```

## Quick summary

| Expression | Meaning |
|---|---|
| `arr[i]` | Access element at index `i` |
| `arr[start:stop:step]` | Slice elements with step size |
| `matrix[r, c]` | Element at row `r`, column `c` |
| `matrix[r, :]` | All columns in row `r` |
| `matrix[:, c]` | All rows in column `c` |

## Practice

The `practice.py` file contains exercises to solve independently. The `lesson.py` file contains working examples.
