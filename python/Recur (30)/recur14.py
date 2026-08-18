def Expression(S, i=0):
    if i == len(S) - 1:
        return int(S[i])

    value = Expression(S, i + 2)

    if S[i + 1] == '+':
        return int(S[i]) + value
    else:
        return int(S[i]) - value


S = input()
print(Expression(S))