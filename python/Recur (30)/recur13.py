def Palindrome(S):
    if len(S) <= 1:
        return True

    if S[0] != S[-1]:
        return False

    return Palindrome(S[1:-1])