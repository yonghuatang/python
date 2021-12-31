t = int(input())

for tc in range(1, t + 1):
    n, d, c, m = map(int, input().split())
    s = input()

    while (len(s) > 0):
        if s[0] == 'D' and d > 0:
            d -= 1
            c += m
        elif s[0] == 'C' and c > 0:
            c -= 1
        else:
            break
        s = s[1:] if (len(s) > 1) else []

    ans = "YES" if ('D' not in s) else "NO"

    print(f"Case #{tc}: {ans}")
