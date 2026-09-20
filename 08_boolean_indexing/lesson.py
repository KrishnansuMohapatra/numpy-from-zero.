import numpy as np

# NumPy Lesson 8: Boolean Indexing

scores = np.array([55, 82, 90, 45, 68, 95, 38, 77])
print("Original scores:", scores)

mask = scores >= 60
print("Passing mask:", mask)
print("Passing scores:", scores[mask])
print("Failing scores:", scores[scores < 60])

honors = scores[(scores >= 80) & (scores <= 95)]
print("Honors scores:", honors)

extreme_scores = scores[(scores < 50) | (scores >= 90)]
print("Scores <50 or >=90:", extreme_scores)

curved_scores = scores.copy()
curved_scores[curved_scores < 60] += 5
print("\nCurved scores:", curved_scores)

labels = np.where(scores >= 60, "Pass", "Fail")
print("Pass/Fail Labels:", labels)
