M = int(input("M (satrlar soni): "))
N = int(input("N (ustunlar soni): "))

matrix = []
print(f"{M}x{N} matritsa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

abs_min = min(sum(matrix, []))

min_col_idx = -1
for j in range(N):
    for i in range(M):
        if matrix[i][j] == abs_min:
            min_col_idx = j
            break
    if min_col_idx != -1:
        break

for row in matrix:
    row.insert(min_col_idx, row[min_col_idx])

print(matrix)