m = int(input())

a = []
for i in range(m):
    a.append(list(map(float, input().split())))

for i in range(m):
    for j in range(m):
        a[i][j] *= not (i < j and i + j > m - 1)

for row in a:
    print(*row)