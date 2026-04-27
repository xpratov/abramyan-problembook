n = int(input("N: "))
a = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

result = []
if n > 0:
    for i in range(n):
        result.append(a[i])
        if i == n - 1 or a[i] != a[i + 1]:
            result.append(0)

print(*result)