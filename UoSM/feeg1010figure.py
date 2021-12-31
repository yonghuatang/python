import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['text.usetex'] = True
mpl.rc('font', family='Arial')

x = np.arange(1,432, 5)
y1 = [129.61,129.68,129.28,128.94,129.11,129.08,129.11,128.27,129.13,128.72,128.84,128.94,
      129.21,128.96,128.82,129.11,129.11,129.24,129.19,128.72,128.57,128.52,128.40,128.08,
      127.00,127.44,126.47,127.22,127.07,126.53,126.38,126.52,126.37,126.31,125.86,125.61,
      125.64,125.59,125.29,125.22,124.95,125.02,124.68,124.88,124.61,124.16,124.29,124.04,
      123.42,123.08,123.25,122.75,122.46,122.66,122.59,122.22,122.22,122.14,121.58,121.79,
      121.48,121.58,121.15,120.98,121.38,121.08,121.01,121.06,120.66,120.69,120.76,119.48,
      120.42,120.59,120.62,120.67,120.27,120.56,120.14,120.62,120.59,120.00,120.42,120.67,
      120.32,120.66,120.64]
y2 = [100.03,98.97,99.88,100.05,99.65,99.98,99.93,99.97,99.01,99.87,100.05,100.07,99.80,99.98,
      99.95,99.92,99.76,99.93,100.12,100.29,100.29,101.45,101.95,102.44,102.78,103.49,104.01,
      103.92,104.51,105.10,105.57,106.04,106.55,106.92,107.26,107.63,108.05,108.30,107.88,
      108.86,109.07,109.83,110.24,110.59,110.27,110.84,111.45,112.04,113.06,113.60,114.14,
      114.73,114.92,115.62,115.81,115.99,116.84,117.21,117.12,117.88,118.00,117.96,118.57,
      118.91,119.02,119.13,119.55,119.95,119.80,120.07,120.83,120.52,120.71,120.76,120.93,
      120.56,120.64,121.04,120.81,121.01,120.74,120.89,121.10,121.11,120.99,121.01,120.86]

fig, ax = plt.subplots(figsize=(7, 5), tight_layout=False)
ax.plot(x, y1, color='b', linestyle='-', label='Tank 1')
ax.plot(x, y2, color='r', linestyle='-', label='Tank 2')

ax.set_xlabel("Elapsed time (s)", fontsize=11)
ax.set_ylabel("Pressure (kPa)", fontsize=11)
ax.set_xlim(xmin=0)
ax.legend()
plt.show()