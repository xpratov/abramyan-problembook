m = int(input())

a = []
for i in range(m):
    a.append(list(map(float, input().split())))

for i in range(m):
    for j in range(m):
        if i * m + j >= (m * m) // 2:
            break
        a[i][j], a[m - 1 - i][m - 1 - j] = a[m - 1 - i][m - 1 - j], a[i][j]

for row in a:
    print(*row)