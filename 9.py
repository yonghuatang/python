for n in range(2, 51):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, 'times', n // x)
            break
    else:
        print(n, 'is a prime number')
print("done")
