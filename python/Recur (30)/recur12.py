def DigitCount(S):
    if S == "":
        return 0

    if S[0].isdigit():
        return 1 + DigitCount(S[1:])

    return DigitCount(S[1:])


for _ in range(5):
    S = input()
    print(DigitCount(S))