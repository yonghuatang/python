import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['text.usetex'] = True
mpl.rc('font', family='Arial')

theta = np.linspace(0, 2*np.pi, 1000)
flux = np.sin(theta)
emf = -2*np.cos(theta)

fig, ax = plt.subplots(figsize=(6, 4), tight_layout=True)
ax.plot(theta, flux, color='g', linestyle='-', label='$\Phi_B$')
ax.plot(theta, emf, color='c', linestyle='-', label='$\mathcal{E}$')

ax.set_xlabel('Rotor angle $\\theta_{\mathrm{rotor}}$ (rad)', fontsize=11)
ax.set_ylabel('\\begin{center}Magnetic flux $\Phi_B$ (Wb)\\\\ Electromotive force $\mathcal{E}$ (V)\end{center}', fontsize=11)
#ax.set_title('Magnetic Flux against Time graph', fontsize=15)
ax.set_xlim(xmin=0, xmax=2*np.pi) #make sure axes starts from zero
#ax.set_ylim(ymin=0)
ax.set_xticks([0, np.pi/2, np.pi, 3/2*np.pi, 2*np.pi])
ax.set_yticks([0, 1, 2/math.sqrt(2), 2])
ax.set_xticklabels(['0', '$\displaystyle\\frac{\pi}{2}$', '$\pi$', '$\displaystyle\\frac{3\pi}{2}$', '$2\pi$'])
ax.set_yticklabels(['0', '$\Phi_{B, \mathrm{max}}$', '$\mathcal{E}_{\mathrm{rms}}$', '$\mathcal{E}_{\mathrm{max}}$'])
ax.legend()
plt.grid()
plt.show()