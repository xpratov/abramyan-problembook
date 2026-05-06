n = int(input("N: "))
a = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

idx = list(range(n))

for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[idx[j]] > a[idx[j+1]]:
            idx[j], idx[j+1] = idx[j+1], idx[j]

result = [x + 1 for x in idx]
print(result)