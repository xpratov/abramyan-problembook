s = input("Butun sonlar fayli: ")

with open(s, "r") as f:
    a = list(map(int, f.read().split()))

a = a[:50]

with open(s, "w") as f:
    for x in a:
        f.write(str(x) + " ")