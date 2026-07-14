M = int(input("Satrlar soni (M): "))
N = int(input("Ustunlar soni (N): "))

matrix = []
print(f"{M}x{N} matrisa elementlarini kiriting:")
for i in range(M):
    row = list(map(int, input().split()))
    matrix.append(row)

first_column = 0

for j in range(N):
  all_odd = True
  for i in range(M):
    if matrix[i][j]%2 == 0:
      all_odd = False
      break
  if all_odd:
    first_column = j+1
    break

print(first_column)