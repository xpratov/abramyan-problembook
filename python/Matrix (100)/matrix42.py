M = int(input("M (satrlar soni): "))
N = int(input("N (ustunlar soni): "))

matrix = []
print(f"{M}x{N} matritsa elementlarini kiriting:")
for i in range(M):
  row = list(map(float, input().split()))
  matrix.append(row)

sorteds = 0
for i in range(M):
  if sorted(matrix[i]) == matrix[i]:
    sorteds += 1

print(sorteds)