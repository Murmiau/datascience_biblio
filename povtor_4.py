import numpy as np

a = np.arange(1, 13)
b = a.reshape(12, 1)
print(b)
print("Количество измерений массива b:", b.ndim)
print("Количество строк и столбцов массива b:", b.shape)

# массив b нельзя назвать одномерным
