# Find Prime Numbers

def findPrimes(n):
    primes = []
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                print(i, " is not a prime number.")
                break
        else:
            print(i, " is a prime number.")
            primes.append(i)
    return primes


# Check prime number

def checkPrime(n):
    if n % 2 == 0:
        return (False, "Divisible by 2")
    for i in range(3, n):
            if n % i == 0:
                return (False, f"Divisible by {i}")
    return (True, "Divisible by None")


if __name__ == "__main__":
    print(findPrimes(100))
    print(checkPrime(177))
