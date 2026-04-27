M = int(input("M (satrlar soni): "))
N = int(input("N (ustunlar soni): "))

matrix = []
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

target_col = -1

for j in range(N):
    all_negative = True
    for i in range(M):
        if matrix[i][j] >= 0:
            all_negative = False
            break
    if all_negative:
        target_col = j
        break  

if target_col != -1:
    for i in range(M):
        matrix[i][target_col], matrix[i][N-1] = matrix[i][N-1], matrix[i][target_col]

print(matrix)