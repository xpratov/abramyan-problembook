M = int(input("M (qatorlar soni) ni kiritig: "))
N = int(input("N (ustunlar soni) ni kiritig: "))

matrix = []

for i in range(M):
  row = []
  for j in range(N):
    row.append(5*(j+1))
  matrix.append(row)

for r in matrix:
  print(*r)