## lambda expressions
## Created by Yonghua 20 Jul 2020

def f(x):
    return 3*x - 1

print(f(5))

# or using lambda expressions,

f = lambda x: 3*x - 1
print(f(5))

### example (quadratic equations)

def quad(a, b, c):
    return lambda x: a*x**2 + b*x + c
result = quad(4, 9, 31)
print(result(35))
