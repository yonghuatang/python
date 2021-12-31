# Polynomial Functions
# Created by YongHua

def f(x):
    return x**4 + 4*x**3 + 8*x**2 - 78*x + 21

while True:
    try:
        number = int(input("Please input a number for the function x**4 + 4*x**3 + 8*x**2 - 78*x + 21.  "))
        print(f(number))
        print("Done.")

    except:
        print("This is not a number! Try again.")


