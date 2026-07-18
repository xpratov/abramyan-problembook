def PosSub(S0, S, K, N):
    if K > len(S):
        return 0

    part = S[K-1:K-1+N]

    pos = part.find(S0)

    if pos == -1:
        return 0

    return K + pos


S0 = input()
S = input()

for i in range(3):
    K, N = map(int, input().split())
    print(PosSub(S0, S, K, N))