n = int(input("N - butun sonini kiriting: "))
a = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

b = a[1::2] + a[::2]

print(b)