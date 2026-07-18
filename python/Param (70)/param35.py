def TrimRightC(S, C):
    i = len(S) - 1

    while i >= 0 and S[i] == C:
        i -= 1

    return S[:i+1]


C = input()

for i in range(5):
    s = input()
    print(TrimRightC(s, C))