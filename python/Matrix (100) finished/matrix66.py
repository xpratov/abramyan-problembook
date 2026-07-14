M = int(input("M (satrlar soni): "))
N = int(input("N (ustunlar soni): "))

matrix = []
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

found = None
for j in range(N):
  negative = True
  for i in range(M):
    if matrix[i][j] > 0:
      negative = False
      break
  if negative:
    found = j

if found is not None:
  for i in range(M):
    matrix[i].pop(found)

print(matrix)
