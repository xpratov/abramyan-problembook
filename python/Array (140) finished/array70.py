n = int(input("N - juft sonini kiriting: "))
a = list(map(float, input(f"{n} ta son kiriting: ").split()))

mid = n // 2 

for i in range(mid):
    a[i], a[i + mid] = a[i + mid], a[i]

print("Natija: ", a)