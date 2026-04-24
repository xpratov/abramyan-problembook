M = int(input("Satrlar soni (M): "))
N = int(input("Ustunlar soni (N): "))

matrix = []
print(f"{M}x{N} matritsa elementlarini kiriting:")
for i in range(M):
    row = list(map(int, input().split()))
    matrix.append(row)

different_rows = 0
for i in range(M):
  if len(set(matrix[i])) == len(matrix[i]):
    different_rows += 1
  
print(different_rows)