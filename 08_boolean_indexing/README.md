# NumPy — Boolean Indexing

## What you'll learn

Boolean indexing lets you filter, select, and modify array values based on logical conditions.

### Boolean Masks

```python
numbers = np.array([10, 25, 40, 5, 60])
mask = numbers > 20
numbers[mask]
```

### Logical Operators

- **`&` AND:** `(arr > 10) & (arr < 50)`
- **`|` OR:** `(arr < 10) | (arr > 80)`
- **`~` NOT:** `~(arr > 50)`

Use parentheses around each condition.

### np.where

```python
grades = np.array([85, 45, 90, 55])
status = np.where(grades >= 60, "Pass", "Fail")
```

## Practice

The `practice.py` file contains exercises to solve independently. The `lesson.py` file contains working examples.
