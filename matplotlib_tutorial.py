import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np

mpl.rc('font', family='Times New Roman')

#csfont = {'fontname':'Arial'}
#hfont = {'fontname':'Arial'}

#------------------------------------------------------------------------------

a=[]
for i in range(1, 4):
    a.append(i**(0.5))
    
b=[1,2,3]
c=[3,4,5]

plt.plot(a, b, color='r', linestyle='--', label='test1')
plt.plot(a, c, color='b', linestyle='-', label='test2')
plt.title("Test Graph of matplotlib", fontsize=14) # **csfont
plt.xlabel("x_axis")  # **hfont
plt.ylabel("y_axis")
plt.legend()
plt.grid(b=True)  #grid lines
plt.show()
