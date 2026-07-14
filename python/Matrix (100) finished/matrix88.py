M = int(input())

A = []
for i in range(M):
    A.append(list(map(float, input().split())))

for i in range(1, M):
    for j in range(i):
        A[i][j] = 0

for row in A:
    print(*row)