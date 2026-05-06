n = int(input("N ni kiriting: "))
a = list(map(float, input(f"{n} ta son kiriting: ").split()))

b = []
c = []

for x in a:
    if x > 0:
        b.append(x)
    elif x < 0:
        c.append(x)

print(len(b), b)

print(len(c), c)