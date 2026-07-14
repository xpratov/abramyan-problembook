M = int(input("M: "))
N = int(input("N: "))

matrix = []
for i in range(M):
    row = list(map(float, input().split()))
    matrix.append(row)

abs_min = None 

for i in range(M):
    current_row = matrix[i]
    if sorted(current_row) == current_row or sorted(current_row, reverse=True) == current_row:
        row_min = min(current_row)
        if abs_min is None or row_min < abs_min:
            abs_min = row_min

if abs_min is None:
    print(0.0)
else:
    print(abs_min)