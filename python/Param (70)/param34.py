def TrimLeftC(S, C):
    i = 0

    while i < len(S) and S[i] == C:
        i += 1

    return S[i:]


C = input()

for i in range(5):
    s = input()
    print(TrimLeftC(s, C))