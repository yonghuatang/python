def natural_numbers(n):
    yield n
    yield from natural_numbers(n+1)


def sieve(s):
    n = next(s)
    yield n
    yield from sieve(i for i in s if i % n != 0)


p = sieve(natural_numbers(2))

for i in range(100):
    print(next(p))
