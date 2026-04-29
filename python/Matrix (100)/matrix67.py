M = int(input("M (satrlar soni): "))
N = int(input("N (ustunlar soni): "))

matrix = []
print(f"{M}x{N} matritsa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

for j in range(N - 1, -1, -1):
    all_positive = True
    
    for i in range(M):
        if matrix[i][j] <= 0: 
            all_positive = False
            break
            
    if all_positive:
        for i in range(M):
            matrix[i].pop(j)

print(matrix)