import numpy as np

mass = np.transpose(np.array([[1, 2, 3, 3, 1],
                           [6, 8, 11, 10, 7]]))

mass

mean_a = np.mean(mass, axis=0)
mean_a

a_centered = mass - mean_a
a_centered

#array([[-1. , -2.4],
#       [ 0. , -0.4],
#       [ 1. ,  2.6],
#       [ 1. ,  1.6],
#       [-1. , -1.4]])
