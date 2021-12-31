import math

t = int(input())

for tc in range(1, t + 1):
    z = int(input())

    # find list of primes, memoisation
    prime = [2]
    for i in range(3, int(math.sqrt(z+1))+10*len(str(z)), 2):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime.append(i)

    for k in range(len(prime)-1):
        num = prime[k] * prime[k+1]
        if num <= z:
            ans = num
        else:
            break

    print(f"Case #{tc}: {ans}")
