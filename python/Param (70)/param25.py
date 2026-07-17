def Transp(A, M):
    for i in range(M):
        for j in range(i + 1, M):
            A[i][j], A[j][i] = A[j][i], A[i][j]


M = int(input())

A = []
for i in range(M):
    A.append(list(map(float, input().split())))

Transp(A, M)

for row in A:
    print(*row)