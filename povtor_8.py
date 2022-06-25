import numpy as np

a = np.zeros((2, 2))
print("массив a:", a)

b = np.ones((3, 2))
print("массив b:", b)

v = np.vstack((a, b))
print("массив v:", v)

print("атрибут size:", v.size)
