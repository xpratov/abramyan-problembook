def ArrayToMatrRow(A, K, M, N):
    B = [[0] * N for _ in range(M)]

    k = 0

    for i in range(M):
        for j in range(N):
            if k < K:
                B[i][j] = A[k]
                k += 1

    return B

K = int(input())
A = list(map(float, input().split()))

M = int(input())
N = int(input())

B = ArrayToMatrRow(A, K, M, N)

for row in B:
    print(*row)