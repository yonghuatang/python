import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['text.usetex'] = True
mpl.rc('font', family='Arial')

if __name__ == "__main__":
    plt.figure(figsize=(6,6),)
    plt.title(r"$\mathbf{D^2 P_T^{}\approx 810}$")
    plt.xlabel(r"$P_T^{}\ [\mathrm{W}]$")
    plt.ylabel(r"$D\ [\mathrm{m}]$")
    plt.xlim(0.0, 100.0)
    plt.ylim(0.0, 100.0)
    plt.plot(arr:=np.linspace(0, 100, 1000), (lambda x: np.sqrt(810/x))(arr), 'r-', linewidth=2)
    # plt.legend(fontsize=8.5, fancybox=False)
    plt.xticks([i * 10 for i in range(11)])
    plt.yticks([i * 10 for i in range(11)])
    plt.grid(alpha=0.25)
    plt.show()