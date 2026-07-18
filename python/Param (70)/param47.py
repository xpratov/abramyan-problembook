def HexToDec(S):
    digits = "0123456789ABCDEF"
    res = 0

    for ch in S:
        res = res * 16 + digits.index(ch)

    return res


for _ in range(5):
    s = input()
    print(HexToDec(s))