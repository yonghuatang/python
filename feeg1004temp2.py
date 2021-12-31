import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['text.usetex'] = True
mpl.rc('font', family='Arial')

x = np.linspace(0, 2*np.pi, 1000)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(6, 4), tight_layout=True)
ax.plot(x, y, color='b', linestyle='-', label='test1')

ax.set_xlabel('Time (s)', fontsize=11)
ax.set_ylabel('Electromotive Force $\ \mathcal{E}$ (V)', fontsize=11)
#ax.set_title('Magnetic Flux against Time graph', fontsize=15)
ax.set_xlim(xmin=0) #make sure axes starts from zero
#ax.set_ylim(ymin=0)
ax.set_xticks([0.5*np.pi, np.pi])
ax.set_yticks([0, 1])
ax.set_xticklabels(['A', 'B'])
ax.set_yticklabels(['0', 'NBA$\omega$'])
#ax.legend()
plt.grid()
plt.show()