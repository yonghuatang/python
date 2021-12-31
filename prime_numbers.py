## prime numbers

primes = []

for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            print(i, " is not a prime number.")
            break
    else:
        print(i, " is a prime number.")
        primes.append(i)

print(primes)
