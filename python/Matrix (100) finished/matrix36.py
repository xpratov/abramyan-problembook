M = int(input("Satrlar soni (M): "))
N = int(input("Ustunlar soni (N): "))

matrix = []
print(f"{M}x{N} matrisa elementlarini kiriting:")
for i in range(M):
    row = list(map(int, input().split()))
    matrix.append(row)

first_row = sorted(set(matrix[0]))

similars = 0
for i in range(1, M):
  if first_row == sorted(set(matrix[i])):
    similars += 1
  
print(similars)