s1 = input("Haqiqiy sonlar fayli: ")
s2 = input("Natija fayli: ")

with open(s1, "r") as f:
    a = list(map(float, f.read().split()))

with open(s2, "w") as f:
    for i in range(1, len(a) - 1):
        if a[i] > a[i - 1] and a[i] > a[i + 1]:
            f.write(str(i + 1) + " ")