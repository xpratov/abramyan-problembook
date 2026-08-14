def UpCaseLat(S):
    result = ""

    for ch in S:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        else:
            result += ch

    return result


for i in range(5):
    s = input()
    print(UpCaseLat(s))