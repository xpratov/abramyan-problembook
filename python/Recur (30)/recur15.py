def Term(S, i):
    value = int(S[i])
    i += 1

    if i < len(S) and S[i] == '*':
        value *= Term(S, i + 1)

    return value


def Expression(S, i=0):
    value = Term(S, i)
    i += 1

    if i < len(S):
        if S[i] == '+':
            return value + Expression(S, i + 1)
        else:
            return value - Expression(S, i + 1)

    return value


S = input()
print(Expression(S))