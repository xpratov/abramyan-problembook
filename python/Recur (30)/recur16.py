def Element(S, i):
    if S[i] == '(':
        value, i = Expression(S, i + 1)
        return value, i + 1

    return int(S[i]), i + 1


def Term(S, i):
    value, i = Element(S, i)

    if i < len(S) and S[i] == '*':
        next_value, i = Term(S, i + 1)
        value *= next_value

    return value, i


def Expression(S, i=0):
    value, i = Term(S, i)

    if i < len(S) and S[i] in '+-':
        next_value, i = Expression(S, i + 1)

        if S[i - 1] == '+':
            value += next_value
        else:
            value -= next_value

    return value, i


S = input()
print(Expression(S)[0])