M = int(input())

A = []
for i in range(M):
    A.append(list(map(float, input().split())))

for i in range(M - 1):
    for j in range(M - i - 1, M):
        A[i][j] = 0

for row in A:
    print(*row)