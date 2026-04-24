M = int(input("Satrlar soni (M): "))
N = int(input("Ustunlar soni (N): "))

matrix = []
print(f"{M}x{N} matrisa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

counts = []
for j in range(N):
  column = []
  for i in range(M):
    column.append(matrix[i][j])
  average = sum(column)/len(column)
  
  count = 0
  for i in range(M):
    if matrix[i][j] > average:
      count += 1
  counts.append(count)

print(counts)