M = int(input("Satrlar soni (M): "))
N = int(input("Ustunlar soni (N): "))

matrix = []
print(f"{M}x{N} matrisa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

mins = []
for i in range(M):
  mins.append(min(matrix[i]))

print(max(mins))