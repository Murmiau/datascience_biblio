import numpy as np

a = np.arange(20, 0, -2)
print(a)


b = np.arange(20, 1, -2).reshape(1, 10)
print(b)

print(f"Размерность массива a: {a.ndim}")
print(f"Размерность массива b: {b.ndim}")
print(a.ndim == b.ndim)

#разница между массивами a и b в размерности (массив a одномерный, массив b двумерный)