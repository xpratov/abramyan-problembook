M = int(input("M (satrlar soni): "))
N = int(input("N (ustunlar soni): "))

matrix = []
print(f"{M}x{N} matritsa elementlarini kiriting (haqiqiy sonlar):")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

elements = sum(matrix, [])

minel = min(elements)
maxel = max(elements)

min_column = 0
max_column = 0

for j in range(N):
  column = []
  for i in range(M):
    column.append(matrix[i][j])
  
  if minel in column:
    min_column = j
  if maxel in column:
    max_column = j

for i in range(M):
  matrix[i][min_column], matrix[i][max_column] = matrix[i][max_column], matrix[i][min_column]

print(matrix)
    