# Function to evaluate factorial using recursion and memoisation

cache = []

def fact(x):
    if x > 2:
        return x * fact(x - 1)
    else:
        return x

if __name__ == "__main__":
    print(fact(10))
    print(fact(100))
