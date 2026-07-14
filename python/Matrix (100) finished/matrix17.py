M = int(input("Satrlar soni (M): "))
N = int(input("Ustunlar soni (N): "))
K = int(input("K - butun sonini kiriting: "))

matrix = []
print(f"{M}x{N} matrisa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

row = matrix[K-1]

summa = 0
prod = 1

for i in row:
  summa+=i
  prod*=i

print(summa, prod)