M = int(input("Satrlar soni (M): "))
N = int(input("Ustunlar soni (N): "))

matrix = []
print(f"{M}x{N} matritsa elementlarini kiriting:")
for i in range(M):
    row = list(map(int, input().split()))
    matrix.append(row)

different_columns = 0

for j in range(N):
  column = []
  for i in range(M):
    column.append(matrix[i][j])
  if len(set(column)) == M:
    different_columns += 1
  
print(different_columns)