M = int(input())

A = []
for i in range(M):
    A.append(list(map(float, input().split())))

for j in range(M):
    s = 0
    cnt = 0
    r = 0
    c = j

    while r < M and c >= 0:
        s += A[r][c]
        cnt += 1
        r += 1
        c -= 1

    print(s / cnt)

for i in range(1, M):
    s = 0
    cnt = 0
    r = i
    c = M - 1

    while r < M and c >= 0:
        s += A[r][c]
        cnt += 1
        r += 1
        c -= 1

    print(s / cnt)