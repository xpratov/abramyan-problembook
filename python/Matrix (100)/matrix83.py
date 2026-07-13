m = int(input())

a = []
for i in range(m):
    a.append(list(map(float, input().split())))

for s in range(2 * m - 1):
    summa = 0
    for i in range(m):
        j = s - i
        if 0 <= j < m:
            summa += a[i][j]
    print(summa)