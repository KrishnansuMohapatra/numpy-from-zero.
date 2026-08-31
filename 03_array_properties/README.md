# NumPy — Array Properties

## What you'll learn

NumPy arrays provide useful properties that describe their structure and data.

### `shape`

Tells you the size of the array along each dimension.

```python
arr.shape
```

Example:

```text
2 rows × 4 columns → (2, 4)
```

### `ndim`

Tells you how many dimensions the array has.

```python
arr.ndim
```

Examples:

- 1D array → `ndim` is `1`
- 2D array → `ndim` is `2`

### `size`

Returns the total number of elements in the array.

```python
arr.size
```

A `(2, 4)` array contains `8` elements.

### `dtype`

Shows the data type stored in the array.

```python
arr.dtype
```

Common examples include integer and floating-point types.

## Quick summary

| Property | Meaning |
|---|---|
| `shape` | Dimensions/size along each axis |
| `ndim` | Number of dimensions |
| `size` | Total number of elements |
| `dtype` | Data type of elements |

## Practice

The `practice.py` file contains exercises to solve independently. The `lesson.py` file contains working examples.
