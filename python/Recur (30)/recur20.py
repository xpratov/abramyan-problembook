def Expression(S, i=0):
    if S[i].isdigit():
        return int(S[i]), i + 1

    function = S[i]
    i += 2  # M( yoki m(

    left, i = Expression(S, i)

    i += 1  # vergulni o'tkazib yuboramiz

    right, i = Expression(S, i)

    i += 1  # ) ni o'tkazib yuboramiz

    if function == 'M':
        return max(left, right), i
    else:
        return min(left, right), i


S = input()
print(Expression(S)[0])