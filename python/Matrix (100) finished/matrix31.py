M = int(input("Satrlar soni (M): "))
N = int(input("Ustunlar soni (N): "))

matrix = []
print(f"{M}x{N} matrisa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

average = sum(sum(matrix, []))/ (M*N)
short_difference = abs(average - matrix[0][0])

column = 0
row = 0

for i in range(M):
  for j in range(N):
    if abs(matrix[i][j] - average) < short_difference:
      column = j
      row = i
      short_difference = abs(matrix[i][j] - average)

print(column+1, row+1)
