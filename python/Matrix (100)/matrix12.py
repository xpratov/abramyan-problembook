M = int(input("Satrlar soni (M): "))
N = int(input("Ustunlar soni (N): "))

matrix = []
print(f"{M}x{N} matrisa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

for j in range(N):
  if j%2==0:
    for i in range(M):
      print(matrix[i][j])
  else:
    for i in range(M-1, -1, -1):
      print(matrix[i][j])
