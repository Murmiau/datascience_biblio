import numpy as np

a = np.arange(0, 12)
print("массив а:", a)

A = a.reshape(4, 3)
print("матрица А:", A)

At = A.T
print("матрица At:", At)

B = np.dot(A, At)
print("матрица B:", B)

print(f"Размер матрицы B: {B.shape[0]}x{B.shape[1]}")

print(np.linalg.inv(B))
# пробуем вычислить обратную матрицу для матрицы B - ошибка

print(np.linalg.matrix_rank(B) < B.shape[0])
# матрица B является вырожденной, т.ч.обратной матрицы для нее нет,
# ранг вырожденной матрицы меньше, чем число ее строк
