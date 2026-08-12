s = input("Haqiqiy sonlar fayli: ")

with open(s, "r") as f:
    a = list(map(float, f.read().split()))

b = a.copy()

for i in range(1, len(a) - 1):
    b[i] = (a[i - 1] + a[i] + a[i + 1]) / 3

with open(s, "w") as f:
    for x in b:
        f.write(str(x) + " ")