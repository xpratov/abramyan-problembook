def Expression(S, i=0):
    if S[i].isdigit():
        return int(S[i]), i + 1

    left, i = Expression(S, i + 1)
    op = S[i]
    i += 1
    right, i = Expression(S, i + 1)

    if op == '+':
        return left + right, i + 1

    if op == '-':
        return left - right, i + 1

    return left * right, i + 1


S = input()
print(Expression(S)[0])