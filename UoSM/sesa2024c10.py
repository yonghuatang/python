import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['text.usetex'] = True
mpl.rc('font', family='Arial')

if __name__ == "__main__":
    plt.title(r"\textit{Temperature profile of one solar array panel over a circular orbit with $\varepsilon_1=23.5^{\circ}$}", size=16)
    plt.xlabel(r"True anomaly, $\theta$ [deg]", size=14)
    plt.ylabel(r"Temperature, $T$ [K]", size=14)
    plt.xlim(0.0, 2*np.pi)
    plt.ylim(327.0, 330.0)
    arr = np.linspace(0, np.pi / 2, 1000)
    arr2 = np.linspace(3 * np.pi/ 2, 2 * np.pi, 1000)
    arr3 = np.linspace(np.pi / 2, 3 * np.pi / 2, 1000)
    plt.plot(arr, (lambda x: (11541438957.476+265718792.867*np.cos(x))**0.25)(arr), 'r-', linewidth=2)
    plt.plot(arr2, (lambda x: (11541438957.476 + 265718792.867 * np.cos(x))**0.25)(arr2), 'r-', linewidth=2)
    plt.plot(arr3, [11541438957.476 ** 0.25]*1000, 'b-', linewidth=2)
    plt.fill_between([0.0, np.pi/2], [327, 327], [330, 330], color='r', alpha=0.02)
    plt.fill_between([np.pi / 2, 3*np.pi/2], [327, 327], [330, 330], color='b', alpha=0.02)
    plt.fill_between([3*np.pi/2, 2*np.pi], [327, 327], [330, 330], color='r', alpha=0.02)
    plt.plot([np.pi/2, np.pi/2], [327, 330], 'k-', alpha=0.4, linewidth=2)
    plt.plot([3*np.pi/2, 3*np.pi/2], [327, 330], 'k-', alpha=0.4, linewidth=2)
    plt.text(np.pi/6+0.1, 329.85, r"Albedo", color='r', fontsize=15, alpha=0.3)
    plt.text(5*np.pi / 3 + 0.1, 329.85, r"Albedo", color='r', fontsize=15, alpha=0.3)
    plt.text(5 * np.pi / 6 + 0.15, 329.85, r"Without albedo", color='b', fontsize=15, alpha=0.3)
    plt.text(np.pi/6+0.125, 327.15, r"$\beta=1$", color='r', fontsize=17, alpha=0.3)
    plt.text(5*np.pi / 3 + 0.125, 327.15, r"$\beta=1$", color='r', fontsize=17, alpha=0.3)
    plt.text(5 * np.pi / 6 + 0.375, 327.15, r"$\beta=0$", color='b', fontsize=17, alpha=0.3)
    # plt.legend(fontsize=8.5, fancybox=False)
    xlabels = [i*30 for i in range(13)]
    plt.xticks([i/6 * np.pi for i in range(13)], xlabels, size=12)
    plt.yticks(size=12)
    plt.grid(alpha=0.25)
    plt.show()