# UoSM Python cheat sheet

import math
import numpy as np
import matplotlib.pyplot as plt

# find roots
from scipy.optimize import bisect, newton, brentq, fsolve

# find minimum
from scipy.optimize import fmin

# interpolation
# from scipy.interpolate import interp1d

# integration
from scipy.integrate import trapz, quad

# ordinary diff. eqs.
from scipy.integrate import odeint

# reverse an array
# arr = [1,2,3,4,5]
# arr[::-1]

# access row/column in 2D array
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# a[i]  <== access rows
# a[:,i]  <== access column

# create array
# np.linspace(0, 100, )  <== (inclusive, inclusive, no. of data points)
#
# create array
# np.arange(x, y, z)  <== (inclusive, exclusive, interval size)
