M = int(input("Satrlar soni (M): "))
N = int(input("Ustunlar soni (N): "))

matrix = []
print(f"{M}x{N} matrisa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

prod_columns = matrix[0]

for row in matrix[1:]:
  for i, val in enumerate(row):
    prod_columns[i]*=val

print(prod_columns)