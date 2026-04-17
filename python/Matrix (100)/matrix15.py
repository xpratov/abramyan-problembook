M = int(input("Satr va ustunlar soni (M): "))

matrix = []
print(f"{M}x{M} matrisa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)
    
top, bottom = 0, M - 1
left, right = 0, M - 1

while top <= bottom:
    for j in range(left, right + 1):
        print(matrix[top][j], end=" ")
    top += 1

    for i in range(top, bottom + 1):
        print(matrix[i][right], end=" ")
    right -= 1

    for j in range(right, left - 1, -1):
        print(matrix[bottom][j], end=" ")
    bottom -= 1

    for i in range(bottom, top - 1, -1):
        print(matrix[i][left], end=" ")
    left += 1
