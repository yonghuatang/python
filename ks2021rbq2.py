t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    disarr = []
    for i in range(len(arr) - 1):
        disarr.append(arr[i + 1] - arr[i])
    num = max(set(disarr), key=disarr.count)
    ans = disarr.count(num) + 1
    print(f"Case #{tc}: {ans}")
