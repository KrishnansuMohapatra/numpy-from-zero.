# NumPy — Broadcasting

## What you'll learn

Broadcasting describes how NumPy handles arithmetic between arrays with different shapes.

### Rules

Two dimensions are compatible when:
1. They are equal, OR
2. One of them is 1.

Otherwise NumPy raises a `ValueError`.

### Examples

```python
arr = np.array([1, 2, 3])
arr + 10
```

A row vector can be applied across every row:

```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])
matrix + np.array([10, 20, 30])
```

A column vector can be applied across every column:

```python
col_vector = np.array([[100], [200]])
matrix + col_vector
```

## Practice

The `practice.py` file contains exercises to solve independently. The `lesson.py` file contains working examples.
