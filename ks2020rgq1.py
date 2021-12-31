t = int(input())
for tc in range(1, t + 1):
    s = str(input())
    kick_count = 0
    start_count = 0
    kick_index = []
    start_index = []
    final_count = 0

    for i in range(0, len(s)):
        try:
            if s[i] == 'K':
                if s[i + 1] == 'I':
                    if s[i + 2] == 'C':
                        if s[i + 3] == 'K':
                            kick_index.append(i)
                    else:
                        continue
                else:
                    continue
            else:
                continue

        except:
            pass

    for i in range(0, len(s)):
        try:
            if s[i] == 'S':
                if s[i + 1] == 'T':
                    if s[i + 2] == 'A':
                        if s[i + 3] == 'R':
                            if s[i + 4] == 'T':
                                start_index.append(i)
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue

        except:
            pass

    for i in kick_index:
        for j in start_index:
            if i < j:
                final_count += 1

    print("Case #{}: {}".format(tc, final_count))

# hope this time doesn't TLE