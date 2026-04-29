M = int(input("M (satrlar soni): "))
N = int(input("N (ustunlar soni): "))

matrix = []
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

found = None
for j in range(N):
  positive = True
  for i in range(M):
    if matrix[i][j] < 0:
      positive = False
      break
  if positive:
    found = j
    break

if found is not None: 
    for i in range(M):
        matrix[i].pop(found)

print(matrix)

