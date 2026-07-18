def PosLast(S0, S):
    pos = S.rfind(S0)

    if pos == -1:
        return 0

    return pos + 1


for i in range(5):
    S0 = input()
    S = input()
    print(PosLast(S0, S))