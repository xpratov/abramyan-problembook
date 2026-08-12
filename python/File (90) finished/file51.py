s1 = input("1-fayl nomi: ")
s2 = input("2-fayl nomi: ")
s3 = input("3-fayl nomi: ")
s4 = input("Yangi fayl nomi: ")

with open(s1, "r") as f:
    a = list(map(float, f.read().split()))

with open(s2, "r") as f:
    b = list(map(float, f.read().split()))

with open(s3, "r") as f:
    c = list(map(float, f.read().split()))

i = j = k = 0
result = []

while i < len(a) or j < len(b) or k < len(c):
    x = a[i] if i < len(a) else float("-inf")
    y = b[j] if j < len(b) else float("-inf")
    z = c[k] if k < len(c) else float("-inf")

    if x >= y and x >= z:
        result.append(x)
        i += 1
    elif y >= x and y >= z:
        result.append(y)
        j += 1
    else:
        result.append(z)
        k += 1

with open(s4, "w") as f:
    f.write(" ".join(map(str, result)))

print("Natija:", result)