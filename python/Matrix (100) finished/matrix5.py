m, n = map(int, input("M va N - butun sonlarini kiriting: ").split())
d = float(input("D - haqiqiy sonini kiriting: "))
numbers = list(map(float, input(f"{m} ta haqiqiy sondan iborat ketma-ketlik kiriting: ").split()))

matrix = []

for i in range(m):
  row = []
  for j in range(n):
    row_item = numbers[i]+d*j
    row.append(row_item)
  matrix.append(row)

for row in matrix:
  print(*row)

