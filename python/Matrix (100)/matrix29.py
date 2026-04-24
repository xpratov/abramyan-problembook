M = int(input("Satrlar soni (M): "))
N = int(input("Ustunlar soni (N): "))

matrix = []
print(f"{M}x{N} matrisa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

counts = []
for i in range(M):
  average = sum(matrix[i])/len(matrix[i])
  count = 0
  for j in range(N):
    if matrix[i][j]<average:
      count+=1
  counts.append(count)

print(counts)