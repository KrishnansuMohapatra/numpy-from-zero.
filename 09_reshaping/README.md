# NumPy — Reshaping

## What you'll learn

Reshaping changes array dimensions without changing the underlying data.

### Rule

The total number of elements must remain the same:

```
original size = new rows × new columns
```

### Inferred Dimension

Use `-1` when NumPy should calculate one dimension:

```python
arr = np.arange(12)
arr.reshape(3, -1)
```

### Flattening

`arr.flatten()` returns a 1D copy.

### Transpose

`arr.T` swaps rows and columns.

### Stacking

- `np.vstack((a, b))` stacks vertically.
- `np.hstack((a, b))` stacks horizontally.

## Practice

The `practice.py` file contains exercises to solve independently. The `lesson.py` file contains working examples.
