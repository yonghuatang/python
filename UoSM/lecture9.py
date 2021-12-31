# Curve fitting

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

def create_data(n):
    """
    Given an integer n, returns n data points x
    and values y as a numpy.array.
    """

    xmax = 5.0
    x = np.linspace(0, xmax, n)
    y = -x ** 2

    # add noise to x-data
    np.random.seed(2)
    y += 1.5 * np.random.normal(size=len(x))

    return x, y

n = 10
x, y = create_data(n)


def model(x, a, b, c):
    """
    Equation to be fitted to the data. The purpose of curve
    fitting is to find the coefficients a, b, c.
    """
    return a * x ** 2 + b * x + c


p, pcov = scipy.optimize.curve_fit(model, x, y)
a, b, c = p

# plot the original data
plt.plot(x, y, 'o', label='data point')

# use finer and regular mesh for fitted plot
xfine = np.linspace(0.1, 4.9, n * 5)

plt.plot(xfine, model(xfine, a, b, c), label='fit')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()