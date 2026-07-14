M = int(input("M (satrlar soni): "))
N = int(input("N (ustunlar soni): "))

matrix = []
print(f"{M}x{N} matritsa elementlarini kiriting (haqiqiy sonlar):")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

for j in range(N):
    column_elements = [matrix[i][j] for i in range(M)]
    
    min_val = min(column_elements)
    max_val = max(column_elements)
    
    idx_min = column_elements.index(min_val)
    idx_max = column_elements.index(max_val)

    matrix[idx_min][j], matrix[idx_max][j] = matrix[idx_max][j], matrix[idx_min][j]

print(matrix)