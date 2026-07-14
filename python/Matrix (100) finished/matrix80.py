M = int(input("M (satrlar soni): "))

matrix = []
print(f"{M}x{N} matritsa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

dia_sum = 0
for i in range(M):
  dia_sum += matrix[i][i]

print(dia_sum)