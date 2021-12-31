t = int(input())

for tc in range(1, t + 1):
    g = int(input())
    ans = 0
    for k in range(1, g+1):
        i = 1
        while True:
            summ = (i/2)*(2*k+i-1)
            if summ == g:
                ans += 1
            if summ > g:
                break
            i += 1

    print(f"Case #{tc}: {ans}")
