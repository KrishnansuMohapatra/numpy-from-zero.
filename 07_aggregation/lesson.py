import numpy as np

# NumPy Lesson 7: Aggregation and Statistics

scores = np.array([85, 92, 78, 64, 88, 95, 73])
print("Scores:", scores)
print("Sum:", np.sum(scores))
print("Mean:", np.mean(scores))
print("Median:", np.median(scores))
print("Standard Deviation:", np.std(scores))
print("Variance:", np.var(scores))
print("Minimum:", np.min(scores))
print("Maximum:", np.max(scores))
print("Index of minimum:", np.argmin(scores))
print("Index of maximum:", np.argmax(scores))

student_grades = np.array([
    [85, 90, 78],
    [70, 65, 80],
    [95, 92, 98],
    [60, 75, 72]
])

print("\nStudent Grades:\n", student_grades)
print("Overall class mean:", np.mean(student_grades))
print("Subject averages (axis=0):", np.mean(student_grades, axis=0))
print("Student averages (axis=1):", np.mean(student_grades, axis=1))
print("Highest scoring student index:",
      np.argmax(np.mean(student_grades, axis=1)))

monthly_sales = np.array([100, 150, 120, 200, 180])
print("\nMonthly Sales:", monthly_sales)
print("Cumulative Sales:", np.cumsum(monthly_sales))
