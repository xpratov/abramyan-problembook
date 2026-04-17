M = int(input("Satr va ustunlar soni (M): "))

matrix = []
print(f"{M}x{M} matrisa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

for k in range(M):
    for i in range(0, M - k):
        print(matrix[i][k])
        
    for j in range(k + 1, M):
        print(matrix[M - 1 - k][j])