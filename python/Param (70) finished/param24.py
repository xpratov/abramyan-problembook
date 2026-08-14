def SwapCol(A, M, N, K1, K2):
    if 1 <= K1 <= N and 1 <= K2 <= N:
        for i in range(M):
            A[i][K1 - 1], A[i][K2 - 1] = A[i][K2 - 1], A[i][K1 - 1]


M = int(input())
N = int(input())

A = []
for i in range(M):
    A.append(list(map(float, input().split())))

K1 = int(input())
K2 = int(input())

SwapCol(A, M, N, K1, K2)

for row in A:
    print(*row)