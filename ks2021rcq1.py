from itertools import permutations

alphabet = "abcdefghijklmnopqrstuvwxyz"

t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    s = input()
    scope = alphabet[0:k]  # [incl:excl]
    possible = [''.join(i[0:n]) for i in permutations(scope)]

    ans = []
    for word in possible:
        if word==word[::-1]:
            ans.append(word)


    print(f"Case #{tc}: {len(ans)}: {ans}")
