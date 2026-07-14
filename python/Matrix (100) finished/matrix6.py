m, n = map(int, input("M va N: ").split())
r = float(input("R: "))
numbers = list(map(float, input(f"{n} ta son: ").split()))

matrix = []

for i in range(m):
    row = []
    for j in range(n):
        row_item = numbers[j] * (r ** i)
        row.append(row_item)
    matrix.append(row)

for row in matrix:
    print(*row)