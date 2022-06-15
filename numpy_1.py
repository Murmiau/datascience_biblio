import numpy as np

mass = np.transpose(np.array([[1, 2, 3, 3, 1],
                           [6, 8, 11, 10, 7]]))

mass

mean_a = np.mean(mass, axis=0)
mean_a

#Нужно ли здесь print(mean_a) писать? Просто в юпитере array выводится и без print,
#а при сохранении в python - нет, хотя библиотеки я скачала.

#array([2. , 8.4])
