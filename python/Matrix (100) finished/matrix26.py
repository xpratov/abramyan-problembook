M = int(input("Satrlar soni (M): "))
N = int(input("Ustunlar soni (N): "))

matrix = []
print(f"{M}x{N} matrisa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

minprod = 1
minprodinx = 0

for j in range(N):
  prod = 1
  for i in range(M):
    prod*=matrix[i][j]
  if prod < minprod:
    minprodinx = j

print(minprod, minprodinx+1)