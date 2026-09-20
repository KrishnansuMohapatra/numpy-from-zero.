# NumPy — Working with Real Data

## What you'll learn

Real-world numerical datasets can be loaded and analyzed using NumPy.

### Loading CSV with np.genfromtxt

```python
data = np.genfromtxt(
    "store_records.csv",
    delimiter=",",
    skip_header=1
)
```

### Extracting Columns

```python
customers = data[:, 1]
revenue = data[:, 2]
expenses = data[:, 3]
```

### Calculations

```python
profit = revenue - expenses
profit_margin = (profit / revenue) * 100
```

## Practice

The `practice.py` file contains exercises to solve independently. The `lesson.py` file contains working examples.
