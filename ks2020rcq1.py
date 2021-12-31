# YongHua 06 April 2021

import re

t = int(input())

for tc in range(1, t + 1):
    ans = 0
    n, k = map(int, input().split())
    arr = input().replace(' ', '')  # makes compact string
    subarr = ""
    for i in range(k, 0, -1):
        subarr += str(i)
    ans = len(re.findall(subarr, arr))
    print(f"Case #{tc}: {ans}")
