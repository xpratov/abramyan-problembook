def DecompressStr(S):
    res = ""
    i = 0

    while i < len(S):
        if i + 1 < len(S) and S[i + 1] == "{":
            ch = S[i]
            i += 2
            num = ""
            while S[i] != "}":
                num += S[i]
                i += 1
            res += ch * int(num)
            i += 1
        else:
            res += S[i]
            i += 1

    return res


for _ in range(5):
    s = input()
    print(DecompressStr(s))