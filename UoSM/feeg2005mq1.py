import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

mpl.rcParams['text.usetex'] = True
mpl.rc('font', family='Arial')

stress = np.log([190, 250, 400, 525, 600])
time = np.log([28695, 5530, 330, 64.5, 28.9])

def f(x, a, b):
    return a*x + b

popt, pcov = curve_fit(f, time, stress)

plt.plot(time, stress, 'x')
plt.plot(new:=np.linspace(0, 11, 11), f(new, *popt))
print(*popt)
plt.xlabel("log(time)")
plt.ylabel("log(stress)")
plt.show()