import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['text.usetex'] = True
mpl.rc('font', family='Arial')

x = np.linspace(0, 2*np.pi, 1000)
y1 = np.sin(x)
y2 = np.sin(x - 2/3*np.pi)
y3 = np.sin(x - 4/3*np.pi)

fig, ax = plt.subplots(figsize=(6, 4), tight_layout=True)
ax.plot(x, y1, color='r', linestyle='-', label='$V_1$')
ax.plot(x, y2, color='b', linestyle='-', label='$V_2$')
ax.plot(x, y3, color='y', linestyle='-', label='$V_3$')

ax.set_xlabel('Time (s)', fontsize=11)
ax.set_ylabel('Voltage (V)', fontsize=11)
#ax.set_title('Magnetic Flux against Time graph', fontsize=15)
ax.set_xlim(xmin=0, xmax=2*np.pi) #make sure axes starts from zero
#ax.set_ylim(ymin=0)
ax.set_xticks([0, 2/3*np.pi, 4/3*np.pi, 2*np.pi])
ax.set_yticks([0, 1/math.sqrt(2), 1])
ax.set_xticklabels(['0', '$\displaystyle\\frac{2\pi}{3\omega}$', '$\displaystyle\\frac{4\pi}{3\omega}$', \
                    '$\displaystyle\\frac{2\pi}{\omega}$'])
ax.set_yticklabels(['0', '$V_{rms}$', '$V_{max}$'])
ax.legend(loc='best', bbox_to_anchor=(0.85, 0.8))
plt.grid()
plt.show()