m, n = map(int, input("M va N: ").split())
matrix = []
print(f"{m} ta qatorni kiriting (har birida {n} tadan son):")
for i in range(m):
    row = list(map(float, input().split()))
    matrix.append(row)

for i in range(1, m, 2):
  print(*matrix[i])