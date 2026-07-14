m = int(input())

a = []
for i in range(m):
    a.append(list(map(float, input().split())))

for i in range(m - 1):
    for j in range(m - 1 - i):
        a[i][j], a[m - 1 - j][m - 1 - i] = a[m - 1 - j][m - 1 - i], a[i][j]

for row in a:
    print(*row)