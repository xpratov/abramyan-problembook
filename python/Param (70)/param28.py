def RemoveRowCol(A, M, N, K, L):
    if K > M or L > N:
        return A, M, N

    del A[K - 1]

    for i in range(M - 1):
        del A[i][L - 1]

    M -= 1
    N -= 1

    return A, M, N


M = int(input())
N = int(input())

A = []
for i in range(M):
    A.append(list(map(float, input().split())))

K = int(input())
L = int(input())

A, M, N = RemoveRowCol(A, M, N, K, L)

print(M, N)
for row in A:
    print(*row)