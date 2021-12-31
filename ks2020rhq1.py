# Solved 22/03/2021 04:27PM (GMT+8) TANG YONG HUA

t = int(input())

for tc in range(1, t+1):
    n, k, s = map(int, input().split())
    restart = k + n
    revert = n + 2*k - 2*s
    ans = min(restart, revert)
    print(f"Case #{tc}: {ans}")