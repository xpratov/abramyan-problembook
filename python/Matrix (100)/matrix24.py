M = int(input("Satrlar soni (M): "))
N = int(input("Ustunlar soni (N): "))

matrix = []
print(f"{M}x{N} matrisa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

maxs = []
for j in range(N):
  column = []
  for i in range(M):
    column.append(matrix[i][j])
  maxs.append(max(column))

print(maxs)
