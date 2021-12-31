# Created by YongHua | 12 April 2021 23:10
# Email: yht1e20@soton.ac.uk

import numpy as np
from math import pi, sin, cos, sqrt


def stress_transformation(exx, eyy, exy, theta):
    """Stress transformation for a 2-D stress tensor matrix.

    Takes four input parameters:
    `exx` >>> the exx stress component.
    `eyy` >>> the eyy stress component.
    `exy` >>> the exy stress component.
    `theta` >>> (in degrees) which is the angle of the stress element to be rotated.

    Returns `exx'`, `eyy'` and `exy'`

    * You can choose to include or omit prefixes e.g. MPa which is 1E6, as always take
      care of units and magnitudes!
    """

    # Convert to radians for the sin and cos functions
    thetar = theta / 180 * pi

    rotation_matrix = np.array([
        [cos(thetar)**2, sin(thetar)**2, sin(2*thetar)],
        [sin(thetar)**2, cos(thetar)**2, -sin(2*thetar)],
        [-cos(thetar)*sin(thetar), cos(thetar)*sin(thetar), cos(2*thetar)]
    ])

    old_stress = np.array([exx, eyy, exy])

    new_stress = np.dot(rotation_matrix, old_stress)

    return new_stress


def find_principle(exx, eyy, exy):
    """Finds the principle values `eI` and `eII` of a 2-D stress element.
    Takes three input parameters: `exx`, `eyy` and `exy`. Returns a list of
    principal stresses"""

    invariant_1 = exx + eyy  # trace
    invariant_2 = exx * eyy - exy ** 2  # determinant

    eI = 0.5 * (invariant_1 + sqrt(invariant_1 ** 2 - 4 * invariant_2))
    eII = 0.5 * (invariant_1 - sqrt(invariant_1 ** 2 - 4 * invariant_2))

    return [eI, eII]  # returns a list


def find_maxshear(exx, eyy, exy):
    """Find the maximum shear stress `exy` in 2-D stress element subject to
    planar rotational transformation. Numerical implementation of Mohr's circle.
    Takes three input parameters: `exx`, `eyy` and `exy`. Returns a list of
    coordinates of maximum shear stresses, in the form [centre, ±radius]"""
    eI, eII = find_principle(exx, eyy, exy)
    centre = (eI + eII) / 2  # centre of Mohr's circle, 0.5tr(e)
    radius = abs(eI - centre)  # radius of Mohr's circle
    assert abs(eI - centre) == abs(eII - centre)
    maxshear = [[centre, radius], [centre, -radius]]
    return maxshear


if __name__ == '__main__':
    # example
    help(stress_transformation)
    print(stress_transformation(40, 860, 375, 30))

    help(find_principle)
    print(find_principle(-25, 75, -56))

    help(find_maxshear)
    print(find_maxshear(-60, -40, 35))

