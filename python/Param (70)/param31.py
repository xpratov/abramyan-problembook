def FillStr(S, N):
    result = ""

    while len(result) < N:
        result += S

    return result[:N]


N = int(input())

for i in range(5):
    s = input()
    print(FillStr(s, N))