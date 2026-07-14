M = int(input("Satrlar soni (M): "))
N = int(input("Ustunlar soni (N): "))

matrix = []
print(f"{M}x{N} matrisa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

print("\nNatija (zigzag tartibda):")

for i in range(M):
    if i % 2 == 0:
        for j in range(N):
            print(matrix[i][j], end=" ")
    else:
        for j in range(N - 1, -1, -1):
            print(matrix[i][j], end=" ")
    
    print()