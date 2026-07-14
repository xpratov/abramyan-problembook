M = int(input("M (satrlar): "))
N = int(input("N (ustunlar): "))

matrix = []
for i in range(M):
    matrix.append(list(map(float, input().split())))

abs_max = None

for j in range(N):
    column = [matrix[i][j] for i in range(M)]
    if column == sorted(column) or column == sorted(column, reverse=True):
        col_max = max(column)
        if abs_max is None or col_max > abs_max:
            abs_max = col_max

if abs_max is None:
    print(0.0)
else:
    print(abs_max)