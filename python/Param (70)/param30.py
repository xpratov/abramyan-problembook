def IsIdent(S):
    if len(S) == 0:
        return -1

    if S[0].isdigit():
        return -2

    for i in range(len(S)):
        if not (S[i].isalpha() or S[i].isdigit() or S[i] == "_"):
            return i + 1

    return 0


for i in range(5):
    s = input()
    print(IsIdent(s))