M = int(input("Satrlar soni (M): "))
N = int(input("Ustunlar soni (N): "))

matrix = []
print(f"{M}x{N} matrisa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

sum_rows = []

for row in matrix:
  summa = 0
  for i in row:
    summa+=i
  sum_rows.append(summa)

print(sum_rows)