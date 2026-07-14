M = int(input("M (satrlar soni): "))
N = int(input("N (ustunlar soni): "))

matrix = []
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

for i in range(M):
    for j in range(N // 2):
        matrix[i][j], matrix[i][N - 1 - j] = matrix[i][N - 1 - j], matrix[i][j]

print(matrix)