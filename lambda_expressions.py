## lambda expressions
## Created by Yonghua - 20 Jul 2020

def f(x):
    return 3*x - 1


# or similarly using lambda expressions

g = lambda x: 3*x - 1


### example (quadratic equations)

def createQuadratic(a, b, c):
    return lambda x: a*x**2 + b*x + c


if __name__ == "__main__":
    print(f(5))
    print(g(5))
    h = createQuadratic(4, 9, 31)  # creates 4*x**2 + 9*x + 31
    print(h(11))
