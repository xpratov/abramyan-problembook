m, n = map(int, input("M va N: ").split())
matrix = []
for i in range(m):
    row = list(map(float, input(f"{i+1}-qator: ").split()))
    matrix.append(row)

for j in range(0, n, 2): 
    for i in range(m):
        print(matrix[i][j])