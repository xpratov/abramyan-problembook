s = input("Haqiqiy sonlar fayli: ")

with open(s, "r") as f:
    a = list(map(float, f.read().split()))

imin = a.index(min(a))
imax = a.index(max(a))

a[imin], a[imax] = a[imax], a[imin]

with open(s, "w") as f:
    for x in a:
        f.write(str(x) + " ")