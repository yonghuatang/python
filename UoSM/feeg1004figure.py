import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['text.usetex'] = True
mpl.rc('font', family='Arial')

resolution = 500000  # the smoothness and accuracy of the plot

omega = np.linspace(1, 1000000, resolution)
R = 1000  # Ohms
C = 10**-5  # Farad

def freqres(omega, R, C):
    return 1 / np.sqrt(1 + (omega * R * C) ** 2)

# plt.plot(omega, freqres(omega, R, C), 'b-', label='test')

plt.semilogx(
    omega,
    freqres(omega, R, C),
    markersize=10,
    color='blue',
    label='$\displaystyle \left|\\frac{\mathbf{V}_{out}}{\mathbf{V}_{in}}\\right|=\\frac{1}{\sqrt{1+(\omega R_{1}C)^{2}}}$'
)

plt.xlabel("Omega")
plt.ylabel("phase")
plt.xlim(1, 1000000)
plt.xlabel('Frequency, $\omega\ (\mathrm{rad\ s^{-1}})$')
plt.ylabel('Gain, $\displaystyle \left|\\frac{\mathbf{V}_{out}}{\mathbf{V}_{in}}\\right|$')
plt.grid(True, which='both')
plt.legend()
plt.show()