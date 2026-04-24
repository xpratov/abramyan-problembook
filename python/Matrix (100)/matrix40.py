M = int(input("Satrlar soni (M): "))
N = int(input("Ustunlar soni (N): "))

matrix = []
for i in range(M):
    row = list(map(int, input().split()))
    matrix.append(row)

max_count_global = 0
last_row_index = 0

for i in range(M):
    current_row = matrix[i]
    max_in_row = 0
    
    for x in set(current_row):
        count = current_row.count(x)
        if count > max_in_row:
            max_in_row = count
            
    if max_in_row >= max_count_global:
        max_count_global = max_in_row
        last_row_index = i + 1

print(last_row_index)