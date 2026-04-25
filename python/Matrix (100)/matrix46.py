
M = int(input("M (satrlar): "))
N = int(input("N (ustunlar): "))

matrix = []
for i in range(M):
    matrix.append(list(map(int, input().split())))

found_element = 0

for i in range(M):
    row_max = max(matrix[i])
    
    for j in range(N):
        if matrix[i][j] == row_max:
            column = [matrix[k][j] for k in range(M)]
            if matrix[i][j] == min(column):
                found_element = matrix[i][j]
                break
    if found_element != 0:
        break

print(found_element)