def CompressStr(S):
    res = ""
    i = 0

    while i < len(S):
        j = i
        while j < len(S) and S[j] == S[i]:
            j += 1

        cnt = j - i

        if cnt >= 4:
            res += S[i] + "{" + str(cnt) + "}"
        else:
            res += S[i] * cnt

        i = j

    return res


for _ in range(5):
    s = input()
    print(CompressStr(s))