def ArrayToMatrCol(A, K, M, N):
    B = [[0] * N for _ in range(M)]

    k = 0

    for j in range(N):
        for i in range(M):
            if k < K:
                B[i][j] = A[k]
                k += 1

    return B

K = int(input())
A = list(map(float, input().split()))

M = int(input())
N = int(input())

B = ArrayToMatrCol(A, K, M, N)

for row in B:
    print(*row)