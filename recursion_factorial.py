# Function to evaluate factorial by recursion

def fact(x):
    if x > 2:
        return x * fact(x - 1)
    else:
        return x


if __name__ == "__main__":
    print(fact(10))
    print(fact(50))
