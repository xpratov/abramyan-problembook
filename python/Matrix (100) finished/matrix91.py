m = int(input())

a = []

for i in range(m):
    row = list(map(float, input().split()))
    a.append(row)

for i in range(m):
    for j in range(m):
        a[i][j] *= (i > j)

for row in a:
    print(*row)