def Expression(S, i=0):
    if S[i].isdigit():
        return int(S[i]), i + 1

    function = S[i]
    i += 2  # M( yoki m(

    values = []
    value, i = Expression(S, i)
    values.append(value)

    while S[i] == ',':
        value, i = Expression(S, i + 1)
        values.append(value)

    i += 1  # )

    if function == 'M':
        return max(values), i

    return min(values), i


S = input()
print(Expression(S)[0])