# NumPy — Aggregation

## What you'll learn

Aggregation functions summarize arrays into totals, averages, variability, and extrema.

| Function | Description |
|---|---|
| `np.sum(a)` | Sum |
| `np.mean(a)` | Average |
| `np.median(a)` | Median |
| `np.std(a)` | Standard deviation |
| `np.var(a)` | Variance |
| `np.min(a)` | Minimum |
| `np.max(a)` | Maximum |
| `np.argmin(a)` | Index of minimum |
| `np.argmax(a)` | Index of maximum |

### Understanding axis

For a 2D array:
- **axis=0:** compute down columns.
- **axis=1:** compute across rows.
- **axis=None:** compute over all elements.

```python
matrix.sum(axis=0)
matrix.sum(axis=1)
```

## Practice

The `practice.py` file contains exercises to solve independently. The `lesson.py` file contains working examples.
