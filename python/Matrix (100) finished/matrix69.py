M = int(input("M (satrlar soni): "))
N = int(input("N (ustunlar soni): "))

matrix = []
print(f"{M}x{N} matritsa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

k = int(input("K - butun sonini kiriting: "))

for i in range(M):
  matrix[i].insert(k, 1)

print(matrix)
