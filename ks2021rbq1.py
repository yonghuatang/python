t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    s = input()

    ans = " 1"
    longest = 1
    for i in range(1, n):
        if s[i] > s[i-1]:
            longest += 1
        else:
            longest = 1
        ans += f" {longest}"

    print(f"Case #{tc}:{ans}")
