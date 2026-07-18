def InvStr(S, K, N):
    if K > len(S):
        return ""

    part = S[K-1:K-1+N]
    return part[::-1]


S = input()

for i in range(3):
    K, N = map(int, input().split())
    print(InvStr(S, K, N))