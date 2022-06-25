import numpy as np

np.random.seed(42)


c = np.arange(0, 16)
print("массив c:", c)


C = c.reshape(4, 4)
print("матрица C:", C)

a = np.arange(0, 12)
A = a.reshape(4, 3)
At = A.T
B = np.dot(A, At)

D = B + C * 10
print("матрица D", D)

D_det = np.linalg.det(D)
D_rank = np.linalg.matrix_rank(D)
D_inv = np.linalg.inv(D)

print(f"Определитель матрицы D: {D_det}")
print(f"Ранг матрицы D: {D_rank}")
print(f"Обратная матрица D_inv:\n {D_inv}")


D_inv[D_inv < 0] = 0
D_inv[D_inv > 0] = 1
print(D_inv)

E = np.where(D_inv == 1, B, C)
print("матрица E", E)
