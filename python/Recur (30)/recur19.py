def Expression(S, i):
    if i >= len(S):
        return False, i

    if S[i].isdigit():
        return True, i + 1

    if S[i] != '(':
        return False, i

    ok, i = Expression(S, i + 1)

    if not ok:
        return False, i

    if i >= len(S):
        return False, i

    if S[i] not in '+-*':
        return False, i

    ok, i = Expression(S, i + 1)

    if not ok:
        return False, i

    if i >= len(S):
        return False, i

    if S[i] != ')':
        return False, i

    return True, i + 1


S = input()

ok, pos = Expression(S, 0)

if ok and pos == len(S):
    print(0)
else:
    print(pos + 1)