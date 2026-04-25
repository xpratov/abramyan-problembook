M = int(input("M (satrlar): "))
N = int(input("N (ustunlar): "))

matrix = []
for i in range(M):
    matrix.append(list(map(int, input().split())))

for i in range(M):
    min_val = min(matrix[i])
    max_val = max(matrix[i])
    
    idx_min = matrix[i].index(min_val)
    idx_max = matrix[i].index(max_val)
    
    matrix[i][idx_min], matrix[i][idx_max] = matrix[i][idx_max], matrix[i][idx_min]

print(matrix)