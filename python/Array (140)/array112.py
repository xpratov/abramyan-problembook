n = int(input("N (<= 6): "))
a = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)