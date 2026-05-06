n = int(input("N: "))
a = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

result = []
if n > 0:
    result.append(0)
    result.append(a[0])
    
    for i in range(1, n):
        if a[i] != a[i-1]:
            result.append(0)
        result.append(a[i])

print(result)