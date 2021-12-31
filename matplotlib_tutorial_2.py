import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['text.usetex'] = True
mpl.rc('font', family='Arial')

x = np.linspace(0.0, 1.0, 100)
y = np.cos(4 * np.pi * x) + 2
z = (1/x) + 1

fig, ax = plt.subplots(figsize=(6, 4), tight_layout=True)
ax.plot(x, y, color='b', linestyle='-', label='test1')
ax.plot(x, z, color='r', linestyle='-', label='test2')

ax.set_xlabel('Time (s)', fontsize=11)
ax.set_ylabel('Velocity $(\mathrm{ms}^{-1})$', fontsize=11)
ax.set_title('Example graph $\displaystyle\sum_{n=1}^\infty'r'\frac{-e^{i\pi}}{2^n}$', fontsize=15)
plt.grid(b=True)
ax.set_xlim(xmin=0) #make sure axes starts from zero
ax.set_ylim(ymin=0)
ax.legend()
plt.show()