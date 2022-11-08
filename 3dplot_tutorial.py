import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

mpl.rcParams['text.usetex'] = True
mpl.rc('font', family='Arial')


if __name__ == "__main__":
    # plt.figure(figsize=(10, 8))
    # plt.gca().set_aspect('equal')
    # plt.title(r"Relationship between corrected mass flow rate $\left(\dot{m}_{\mathrm{corr}}\right)$ and absolute upstream stagnation pressure $(p_0)$", pad=20, size=14)
    # plt.xlabel(r"Absolute upstream stagnation pressure, $p_0\ $ [bar]", labelpad=10, size=14)
    # plt.ylabel(r"Corrected mass flow rate, $\dot{m}_{\mathrm{corr}}\ $ [g/s]", labelpad=10, size=14)
    # plt.xlim(0.0, 7.0)
    # plt.ylim(0.0, 4.0)
    # plt.xticks(size=11)
    # plt.yticks(size=11)
    # plt.grid(alpha=0.25)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    theta = np.linspace(-5 * np.pi, 5 * np.pi, 100)
    z = np.linspace(0, 2, 100)
    r = z
    x = np.e**(-r) * np.sin(theta)
    y = np.e**(-r) * np.cos(theta)
    ax.plot(x, y, z, label='parametric curve', zdir='z')
    ax.set_zlim(0, 2)
    ax.legend()

    plt.show()

