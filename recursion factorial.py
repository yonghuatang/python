def fact(x):
    if x > 0:
        return x * fact(x - 1)
    elif x == 0:
        return 1
    
