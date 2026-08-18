def Arguments(S, i, operation):
    value, i = Expression(S, i)

    if S[i] == ',':
        rest, i = Arguments(S, i + 1, operation)

        if operation == 'And':
            value = value and rest
        else:
            value = value or rest

    return value, i


def Expression(S, i=0):
    if S[i] == 'T':
        return True, i + 1

    if S[i] == 'F':
        return False, i + 1

    if S[i:i + 3] == 'And':
        value, i = Arguments(S, i + 4, 'And')
        return value, i + 1

    if S[i:i + 2] == 'Or':
        value, i = Arguments(S, i + 3, 'Or')
        return value, i + 1

    # Not(
    value, i = Expression(S, i + 4)
    return not value, i + 1


S = input()
print(Expression(S)[0])