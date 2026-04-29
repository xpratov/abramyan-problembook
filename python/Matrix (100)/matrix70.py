M = int(input("M (satrlar soni): "))
N = int(input("N (ustunlar soni): "))

matrix = []
print(f"{M}x{N} matritsa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

max_el = matrix[0][0]
max_row_index = 0

for i in range(M):
    for j in range(N):
        if matrix[i][j] > max_el:
            max_el = matrix[i][j]
            max_row_index = i

matrix.insert(max_row_index + 1, matrix[max_row_index][:])

print(matrix)