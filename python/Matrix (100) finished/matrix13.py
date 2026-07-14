M = int(input("Satr va ustunlar soni (M): "))

matrix = []
print(f"{M}x{M} matrisa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

for k in range(M):
    for j in range(0, M - k):
        print(matrix[k][j])
        
    for i in range(k + 1, M):
        print(matrix[i][M - 1 - k])