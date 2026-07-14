M = int(input("Satrlar soni (M): "))
N = int(input("Ustunlar soni (N): "))

matrix = []
print(f"{M}x{N} matrisa elementlarini kiriting:")
for i in range(M):
    row = list(map(int, input().split()))
    matrix.append(row)

last_row = 0

for i in range(M):
  all_even = True
  for j in range(N):
    if matrix[i][j]%2 == 1:
      all_even = False
      break
  if all_even:
    last_row = i+1

print(last_row)
