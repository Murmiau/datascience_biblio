import numpy as np

a = np.arange(12, 24)
print("массив а", a)


a_1 = a.reshape(1, 12)
a_2 = a.reshape(2, 6)
a_3 = a.reshape(3, 4)
a_4 = a.reshape(4, 3)
a_5 = a.reshape(6, 2)

an = [a_1, a_2, a_3, a_4, a_5]
for n in an:
    print("ndim =", n.ndim)


a1 = a.reshape(4, -1)
a2 = a.reshape(-1, 6)
a3 = a.reshape(12, -1)
a4 = a.reshape(-1, 4)
a5 = a.reshape(2, -1)

an = [a1, a2, a3, a4, a5]
for n in an:
    print("ndim =", n.ndim)
