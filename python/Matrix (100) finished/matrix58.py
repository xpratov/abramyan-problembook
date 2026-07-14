M = int(input("M (satrlar soni): "))
N = int(input("N (ustunlar soni): "))

matrix = []
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

for i in range(M // 2):
    for j in range(N // 2):
        matrix[i][j + N // 2], matrix[i + M // 2][j] = matrix[i + M // 2][j], matrix[i][j + N // 2]

print(matrix)