M = int(input())

A = []
for i in range(M):
    A.append(list(map(float, input().split())))

for j in range(M - 1, -1, -1):
    mn = A[0][j]
    r = 0
    c = j

    while r < M and c < M:
        if A[r][c] < mn:
            mn = A[r][c]
        r += 1
        c += 1

    print(mn)

for i in range(1, M):
    mn = A[i][0]
    r = i
    c = 0

    while r < M and c < M:
        if A[r][c] < mn:
            mn = A[r][c]
        r += 1
        c += 1

    print(mn)