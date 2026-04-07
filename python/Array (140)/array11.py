n = int(input("N - butun sonini kiriting: "))
a = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))
k = int(input("K - butun sonini kiriting: "))

print(a[k-1::k])

