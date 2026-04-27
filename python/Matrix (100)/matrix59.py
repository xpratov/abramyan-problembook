M = int(input("M (satrlar soni): "))
N = int(input("N (ustunlar soni): "))

matrix = []
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

for i in range(M//2):
  matrix[i], matrix[M-1-i] = matrix[M-1-i], matrix[i]

print(matrix)