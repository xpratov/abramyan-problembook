m, n = map(int, input("M va N: ").split())
matrix = []
print(f"{m} ta qatorni kiriting (har birida {n} tadan son):")
for i in range(m):
    row = list(map(float, input().split()))
    matrix.append(row)

k = int(input("K (chiqarilishi kerak bo'lgan qator tartibi): "))

if 1 <= k <= m:
    print(*(matrix[k-1]))
else:
    print("Xato: K soni qatorlar sonidan katta yoki noto'g'ri!")