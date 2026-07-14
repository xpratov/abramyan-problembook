M = int(input("Satrlar soni (M): "))
N = int(input("Ustunlar soni (N): "))

matrix = []
print(f"{M}x{N} matrisa elementlarini kiriting:")
for i in range(M):
    row = list(map(int, input().split()))
    matrix.append(row)

nulby = 0

for j in range(N):
  negatives = 0
  positives = 0
  for i in range(M):
    if matrix[i][j]<0:
      negatives += 1
    elif matrix[i][j]>0:
      positives += 1
  if negatives==positives:
    nulby = j+1

print(nulby)
