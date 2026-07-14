M = int(input())

A = []
for i in range(M):
    A.append(list(map(float, input().split())))

for j in range(M):
    mx = A[0][j]
    r = 0
    c = j

    while r < M and c >= 0:
        if A[r][c] > mx:
            mx = A[r][c]
        r += 1
        c -= 1

    print(mx)

for i in range(1, M):
    mx = A[i][M - 1]
    r = i
    c = M - 1

    while r < M and c >= 0:
        if A[r][c] > mx:
            mx = A[r][c]
        r += 1
        c -= 1

    print(mx)