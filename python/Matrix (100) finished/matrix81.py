m = int(input())

a = []
for _ in range(m):
    a.append(list(map(float, input().split())))

s = 0
for i in range(m):
    s += a[i][m - 1 - i]

print(s / m)