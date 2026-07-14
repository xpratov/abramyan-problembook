M = int(input("M (satrlar soni): "))
N = int(input("N (ustunlar soni): "))

matrix = []
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

for j in range(N//2):
  for i in range(M):
    matrix[i][j], matrix[i][j + N//2] = matrix[i][j + N//2], matrix[i][j]

print(matrix)