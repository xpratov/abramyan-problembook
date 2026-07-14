M = int(input("M (qatorlar soni) ni kiritig: "))
N = int(input("N (ustunlar soni) ni kiritig: "))
numbers = list(map(float, input(f"{M} ta haqiqiy son kiriting: ").split()))

matrix = []

for i in range(M):
  row = []
  for j in range(N):
    row.append(numbers[i])
  matrix.append(row)

for row in matrix:
  print(*row)
