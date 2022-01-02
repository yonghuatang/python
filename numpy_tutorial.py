import numpy as np

# One-dimensional array

a = np.array([1, 2, 3])
# print(a)

b = np.array([1., 2., 3.])   # float instead of int
# print(b)

a.ndim   # get dimension

b.shape  # get shape

c = np.array([
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
	])

c[1, 2]   # get a specific element in the matrix *remember that counting starts from 0!!!*

c[1, :]   # get a specific row

c[:, 1]   # get a specific column
