s = input("Butun sonlar fayli: ")

with open(s, "r") as f:
    a = list(map(int, f.read().split()))

b = []

i = 0
j = len(a) - 1

while i <= j:
    b.append(a[i])

    if i != j:
        b.append(a[j])

    i += 1
    j -= 1

with open(s, "w") as f:
    for x in b:
        f.write(str(x) + " ")