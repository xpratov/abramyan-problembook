M = int(input("Satrlar soni (M): "))
N = int(input("Ustunlar soni (N): "))

matrix = []
print(f"{M}x{N} matrisa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

maxs = []
for j in range(N):
  columns = []
  for i in range(M):
    columns.append(matrix[i][j])
  maxs.append(max(columns))

print(min(maxs))