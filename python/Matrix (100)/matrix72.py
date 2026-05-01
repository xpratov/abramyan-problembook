M = int(input("M (satrlar soni): "))
N = int(input("N (ustunlar soni): "))

matrix = []
print(f"{M}x{N} matritsa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

first_col = None

for j in range(N):
  positive = True
  for i in range(M):
    if matrix[i][j] < 0:
      positive = False
      break
  if positive:
    first_col = j
    break

if first_col is not None:
  for i in range(M):
    matrix[i].insert(first_col, 1)

print(matrix)