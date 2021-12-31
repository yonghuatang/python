import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['text.usetex'] = True
mpl.rc('font', family='Arial')

x1 = np.linspace(0, 2, 1000)
x2 = np.linspace(2, 4, 1000)
y1 = x1
y2 = -x2+4

fig, ax = plt.subplots(figsize=(6, 4), tight_layout=True)
ax.plot(x1, y1, color='b', linestyle='-', label='test1')
ax.plot(x2, y2, color='b', linestyle='-', label='test1')

ax.set_xlabel('Time (s)', fontsize=11)
ax.set_ylabel('Magnetic Flux $\Phi_B$ (Wb)', fontsize=11)
#ax.set_title('Magnetic Flux against Time graph', fontsize=15)
ax.set_xlim(xmin=0) #make sure axes starts from zero
ax.set_ylim(ymin=0)
ax.set_xticks([1, 2])
ax.set_yticks([0, 2])
ax.set_xticklabels(['A', 'B'])
ax.set_yticklabels(['0','$BA$'])
#ax.legend()
plt.grid()
plt.show()