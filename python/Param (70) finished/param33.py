def LowCaseLat(S):
    result = ""

    for ch in S:
        if 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch

    return result


for i in range(5):
    s = input()
    print(LowCaseLat(s))