def RemoveRows(A, M, N, K1, K2):
    if K1 > M:
        return A, M

    if K2 > M:
        K2 = M

    del A[K1 - 1:K2]

    M = len(A)

    return A, M


M = int(input())
N = int(input())

A = []
for i in range(M):
    A.append(list(map(float, input().split())))

K1 = int(input())
K2 = int(input())

A, M = RemoveRows(A, M, N, K1, K2)

print(M)

for row in A:
    print(*row)