import numpy as np

# NumPy Lesson 6: Broadcasting

arr = np.array([10, 20, 30])
print("Original array:", arr)
print("arr + 5:", arr + 5)

matrix = np.array([[1, 2, 3], [4, 5, 6]])
row_vector = np.array([10, 20, 30])

print("\nMatrix:\n", matrix)
print("Row vector:", row_vector)
print("Matrix + row vector:\n", matrix + row_vector)

col_vector = np.array([[100], [200]])
print("\nColumn vector shape:", col_vector.shape)
print("Matrix + col vector:\n", matrix + col_vector)

exam_scores = np.array([
    [75, 80, 90],
    [85, 70, 95],
    [90, 88, 92]
])
subject_means = np.mean(exam_scores, axis=0)
centered_scores = exam_scores - subject_means

print("\nExam scores:\n", exam_scores)
print("Subject means:", subject_means)
print("Centered scores:\n", np.round(centered_scores, 2))
