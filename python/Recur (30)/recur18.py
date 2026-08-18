def Expression(S, i):
    if i >= len(S):
        return False, i

    if S[i].isdigit():
        return True, i + 1

    if S[i] != '(':
        return False, i

    left_ok, i = Expression(S, i + 1)

    if not left_ok or i >= len(S):
        return False, i

    if S[i] not in '+-*':
        return False, i

    right_ok, i = Expression(S, i + 1)

    if not right_ok or i >= len(S):
        return False, i

    if S[i] != ')':
        return False, i

    return True, i + 1


S = input()
ok, pos = Expression(S, 0)

print(ok and pos == len(S))