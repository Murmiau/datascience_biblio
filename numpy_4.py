import numpy as np

mass = np.transpose(np.array([[1, 2, 3, 3, 1],
                           [6, 8, 11, 10, 7]]))
mass

mean_a = np.mean(mass, axis=0)
mean_a

a_centered = mass - mean_a
a_centered

a_centered_sp = (a_centered[:, 0] @ a_centered[:, 1]) / (a_centered.shape[0] - 1)
a_centered_sp

np.cov(mass.transpose())[0, 1]

# 2.0
