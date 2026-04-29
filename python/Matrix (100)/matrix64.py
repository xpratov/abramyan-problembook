M = int(input("M (satrlar soni): "))
N = int(input("N (ustunlar soni): "))

matrix = []
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

maxcol = 0
maxel = matrix[0][0]

for i in range(M):
  for j in range(N):
    if maxel < matrix[i][j]:
      maxcol = j
      maxel = matrix[i][j]

for i in range(M):
  matrix[i].pop(maxcol)

print(matrix)
