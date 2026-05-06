n = int(input("N - butun sonini kiriting: "))
a = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))
b = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

a, b = b, a

print(a, b)