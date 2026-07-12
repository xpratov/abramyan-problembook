m = int(input())

a = []
for _ in range(m):
    a.append(list(map(float, input().split())))

for k in range(m - 1, -m, -1):
    s = 0
    for i in range(m):
        j = i + k
        if 0 <= j < m:
            s += a[i][j]
    print(s)