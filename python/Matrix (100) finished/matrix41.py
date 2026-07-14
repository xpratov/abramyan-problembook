M = int(input("M (satrlar soni): "))
N = int(input("N (ustunlar soni): "))

matrix = []
print(f"{M}x{N} matritsa elementlarini kiriting:")
for i in range(M):
    row = list(map(int, input().split()))
    matrix.append(row)

max_equal_count = -1 
first_col_index = 0  

for j in range(N):
    current_column = []
    for i in range(M):
        current_column.append(matrix[i][j])

    current_max_equal = 0
    for x in set(current_column):
        count = current_column.count(x)
        if count > current_max_equal:
            current_max_equal = count

    if current_max_equal > max_equal_count:
        max_equal_count = current_max_equal
        first_col_index = j + 1 

print(f"Eng ko'p bir xil elementli birinchi ustun tartib raqami: {first_col_index}")
