m = int(input())

a = []
for i in range(m):
    a.append(list(map(float, input().split())))

for i in range(m):
    for j in range(i + 1, m):
        a[i][j], a[j][i] = a[j][i], a[i][j]

for j in range(m):
    for i in range(m // 2):
        a[i][j], a[m - 1 - i][j] = a[m - 1 - i][j], a[i][j]

for row in a:
    print(*row)