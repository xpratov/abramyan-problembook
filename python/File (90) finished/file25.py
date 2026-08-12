s = input("Haqiqiy sonlar fayli: ")

with open(s, "r") as f:
    a = list(map(float, f.read().split()))

for i in range(len(a)):
    a[i] = a[i] ** 2

with open(s, "w") as f:
    for x in a:
        f.write(str(x) + " ") 