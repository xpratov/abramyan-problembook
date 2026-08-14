def Chessboard(M, N):
    A = [[0] * N for _ in range(M)]

    for i in range(M):
        for j in range(N):
            A[i][j] = (i + j) % 2

    return A

M = int(input())
N = int(input())

A = Chessboard(M, N)

for row in A:
    print(*row)