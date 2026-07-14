M = int(input("Satrlar soni (M): "))
N = int(input("Ustunlar soni (N): "))

matrix = []
print(f"{M}x{N} matrisa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

max_row = 0
max_sum = sum(matrix[0])

for i in range(M):
  if sum(matrix[i])>max_sum:
    max_sum = sum(matrix[i])
    max_row = i

print(max_row+1, max_sum)