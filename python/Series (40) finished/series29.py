k, n = map(int, input("K va N ni kiriting: ").split())

summa = 0

for i in range(k):
    qator = list(map(int, input(f"{i + 1}-ketma-ketlikni kiriting: ").split()))
    
    for j in range(n):
        summa += qator[j]

print(summa)