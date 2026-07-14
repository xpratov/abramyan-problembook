M = int(input("M (satrlar soni): "))
N = int(input("N (ustunlar soni): "))

matrix = []
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

target_col = -1

for j in range(N):
    all_positive = True
    for i in range(M):
        if matrix[i][j] <= 0:
            all_positive = False
            break
    if all_positive:
        target_col = j

if target_col != -1:
    for i in range(M):
        matrix[i][0], matrix[i][target_col] = matrix[i][target_col], matrix[i][0]

print(matrix)