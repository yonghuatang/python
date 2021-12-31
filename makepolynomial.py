# Created by YongHua - 22 Feb 2021

class Polynomial:

    def __init__(self, *args):
        self.coefficients = [*args]
        print("Created a polynomial function.")
        for i in range(len(self.coefficients) - 1):
            print("a{} = {}".format(i, self.coefficients[i]), end=', ')
        print("a{} = {}".format(len(self.coefficients) - 1, self.coefficients[-1]))


    def __add__(self, other):
        order = max(len(self.coefficients), len(other.coefficients))
        pass


    def show(self):
        if str(self.coefficients[0])[0] == '-':
            print("-", end=' ')
            print("{}*x**{}".format(str(self.coefficients[0])[1:], len(self.coefficients) - 1), end=' ')
        else:
            print("{}*x**{}".format(str(self.coefficients[0]), len(self.coefficients) - 1), end=' ')

        for i in range(1, len(self.coefficients) - 1):
            if str(self.coefficients[i])[0] == '-':
                print("-", end=' ')
                print("{}*x**{}".format(str(self.coefficients[i])[1:], len(self.coefficients) - 1 - i), end=' ')
            else:
                print("+", end=' ')
                print("{}*x**{}".format(self.coefficients[i], len(self.coefficients) - 1 - i), end=' ')

        if str(self.coefficients[-1])[0] == '-':
            print("-", end=' ')
            print(str(self.coefficients[-1])[1:])
        else:
            print("+", end=' ')
            print(self.coefficients[-1])


    def calc(self, x):
        ans = 0
        length = len(self.coefficients)
        for i in range(length):
            ans += self.coefficients[i] * x ** (length - 1 - i)
        return ans


f = Polynomial(-1, 2, -1)
print(f.coefficients)
f.show()
f.calc(123)