# Created by YongHua
# 05 November 2020
# Python 3.8

import numpy as np

"Sequence as black, silver, red, blue, green, white."
a = np.array([0.248, 0.217, 0.133, 0.211, 0.024, 0.167])

b = np.array([
    [.6, .1, .06, .1, .04, .1],
    [.1, .7, .02, .02, .06, .1],
    [.2, .1, .5, .06, .04, .1],
    [.2, .03, .3, .4, .06, .01],
    [.01, .01, .1, .4, .4, .08],
    [.1, .05, .01, .01, .03, .8]
])

def matrix_multiplication(A, B, n):
    """A function that returns another matrix
    after multiplying matrix A and matrix B
    n times."""
    while n:
        A_new = np.dot(A, B)
        n -= 1
        A = A_new
    return list(A_new)

print(matrix_multiplication(a, b, 25))

ans = max(matrix_multiplication(a, b, 25))
print("The most popular car is", ans)  # White
