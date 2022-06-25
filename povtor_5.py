import numpy as np

a = np.random.randn(3, 4)
print("1-й массив:", a)

b = a.flatten()
print("2-й массив:", b)

a.size == b.size
