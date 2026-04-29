M = int(input("M (satrlar soni): "))
N = int(input("N (ustunlar soni): "))

matrix = []
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

minrow = 0
minel = matrix[0][0]

for i in range(M):
  for j in range(N):
    if minel>matrix[i][j]:
      minrow = i
      minel = matrix[i][j]
  
matrix.pop(minrow)

print(matrix)