M = int(input("M (satrlar soni): "))
N = int(input("N (ustunlar soni): "))

matrix = []
print(f"{M}x{N} matritsa elementlarini kiriting:")
for i in range(M):
  row = list(map(float, input().split()))
  matrix.append(row)

sorteds = 0
for j in range(N):
  isSorted = True
  last = matrix[0][j]
  for i in range(1, M):
    if matrix[i][j]>last:
      isSorted = False
      break
    last = matrix[i][j]
  if isSorted:  
    sorteds +=1

print(sorteds)

