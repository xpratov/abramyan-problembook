def BinToDec(S):
    res = 0

    for ch in S:
        res = res * 2 + int(ch)

    return res


for _ in range(5):
    s = input()
    print(BinToDec(s))