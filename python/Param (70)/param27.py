def RemoveCols(A, M, N, K1, K2):
    if K1 > N:
        return A, N

    if K2 > N:
        K2 = N

    for i in range(M):
        del A[i][K1 - 1:K2]

    N = len(A[0]) if M > 0 else 0

    return A, N


M = int(input())
N = int(input())

A = []
for i in range(M):
    A.append(list(map(float, input().split())))

K1 = int(input())
K2 = int(input())

A, N = RemoveCols(A, M, N, K1, K2)

print(N)
for row in A:
    print(*row)