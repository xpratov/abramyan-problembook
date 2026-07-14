
M = int(input())

A = []
for i in range(M):
    row = list(map(float, input().split()))
    A.append(row)

for j in range(M - 1, -1, -1):
    s = 0
    cnt = 0
    i = 0
    k = j

    while i < M and k < M:
        s += A[i][k]
        cnt += 1
        i += 1
        k += 1

    print(s / cnt)

for i in range(1, M):
    s = 0
    cnt = 0
    r = i
    c = 0

    while r < M and c < M:
        s += A[r][c]
        cnt += 1
        r += 1
        c += 1

    print(s / cnt)