m = int(input())

a = []
for i in range(m):
    a.append(list(map(float, input().split())))

for i in range(m):
    for j in range(i + 1, m):
        a[i][j], a[j][i] = a[j][i], a[i][j]

for i in range(m):
    for j in range(m // 2):
        a[i][j], a[i][m - 1 - j] = a[i][m - 1 - j], a[i][j]

for row in a:
    print(*row)