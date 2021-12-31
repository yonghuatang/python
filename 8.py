from math import sqrt, sin, pi
x = 0.0; s = 0.0
for i in range(101):
    s = s + sqrt(x)*sin(x)
    x = x + 0.01*pi
print(s)

def zeta(x):
    for n in range(1: infinity):
    
