m, n = map(int, input("M va N: ").split())
matrix = []
print(f"{m} ta qatorni kiriting (har birida {n} tadan son):")
for i in range(m):
    row = list(map(float, input().split()))
    matrix.append(row)

k = int(input("K (chiqarilishi kerak bo'lgan ustun tartibi): "))

column = []
for row in matrix:
  column.append(row[k-1])

print(*column)