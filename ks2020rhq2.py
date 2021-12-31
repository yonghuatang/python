t = int(input())

def solve(i):
    isBoring = True
    cache = [*str(i)]
    for i in range(0, len(cache)):
        if i % 2 == 0:
            if int(cache[i]) % 2 == 0:
                isBoring = False
                break
        else:
            if int(cache[i]) % 2 != 0:
                isBoring = False
                break
    return isBoring


for tc in range(1, t + 1):
    l, r = map(int, input().split())
    ans = 0
    for i in range(l, r + 1):
        ans += solve(i)
    print(f"Case #{tc}: {ans}")
