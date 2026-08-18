def Expression(S, i=0):
    if S[i] == 'T':
        return True, i + 1

    if S[i] == 'F':
        return False, i + 1

    if S[i:i + 3] == 'And':
        i += 4  # And(

        left, i = Expression(S, i)
        i += 1  # ,

        right, i = Expression(S, i)
        i += 1  # )

        return left and right, i

    if S[i:i + 2] == 'Or':
        i += 3  # Or(

        left, i = Expression(S, i)
        i += 1  # ,

        right, i = Expression(S, i)
        i += 1  # )

        return left or right, i


S = input()
print(Expression(S)[0])