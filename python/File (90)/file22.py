s1 = input("Haqiqiy sonlar fayli: ")
s2 = input("Natija fayli: ")

with open(s1, "r") as f:
    a = list(map(float, f.read().split()))

indexes = []

for i in range(1, len(a) - 1):
    if (a[i] > a[i - 1] and a[i] > a[i + 1]) or \
       (a[i] < a[i - 1] and a[i] < a[i + 1]):
        indexes.append(i + 1)

with open(s2, "w") as f:
    for x in reversed(indexes):
        f.write(str(x) + " ")