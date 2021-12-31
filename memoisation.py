# For a recursive function, time needed to compute is linked to the recursion depth.
# In this example, we will demonstrate the usual method of defining a recursive function,
# and another one using memoisation, which speeds up the computation.

# Define a Fibonacci function the usual way
def fibonacci(n):
    """
    Takes an integer n and returns the n-th term
    of Fibonacci series.
    """
    try:
        type(n) == int and n >= 1
    except:
        raise ValueError("Please input a positive integer.")
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Call the function (takes quite a long time for big numbers)
print(fibonacci(20))

# Now we use memoisation method
# initialise a dictionary that store values that are evaluated previously,
# so the program doesn't need to compute it all over again.

cache = {}

def fibonacci2(n):
    """
    Takes an integer n and returns the n-th term
    of Fibonacci series.
    """
    if n in cache:
        return cache[n]
    try:
        type(n) == int and n >= 1
    except:
        raise ValueError("Please input a positive integer!")
    if n == 1 or n == 2:
        return 1
    else:
        ans = fibonacci2(n-1) + fibonacci2(n-2)
        cache[n] = ans  # store the value in cache if it previously not exists
        return ans

# Call the function with lightning speed. No problem for acceptably large numbers.
print(fibonacci2(300))