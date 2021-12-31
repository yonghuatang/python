import numpy as np
import statics2


lhs = np.array([
    [0.8214, 0.1786, 0.7760],
    [0.2500, 0.7500, 0.8660],
    [0.5868, 0.4132, -0.9848]
])

rhs = np.array([
    [-152],
    [27],
    [253]
]) * 1E-6  # factor here!


ans = np.dot(np.linalg.inv(lhs), rhs)

if __name__ == '__main__':
    print(ans)
    print(statics2.stress_transformation(-15, -4, -1.6, 0))


