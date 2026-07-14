M = int(input("Satrlar soni (M): "))
N = int(input("Ustunlar soni (N): "))

matrix = []
print(f"{M}x{N} matritsa elementlarini kiriting:")
for i in range(M):
    row = list(map(int, input().split()))
    matrix.append(row)

last_col_set = set(matrix[i][N-1] for i in range(M))

similars = 0
for j in range(N - 1):
    current_col_set = set(matrix[i][j] for i in range(M))
    if current_col_set == last_col_set:
        similars += 1

print(similars)