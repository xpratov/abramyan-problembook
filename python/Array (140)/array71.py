n = int(input("N ni kiriting: "))
a = list(map(float, input(f"{n} ta son kiriting: ").split()))

for i in range(n // 2):
    a[i], a[n - 1 - i] = a[n - 1 - i], a[i]

print(a)