s = input("Fayl nomini kiriting: ")

with open(s, "r") as f:
    components = f.read().split()

result = []

for x in components:
    result.append(x)
    if 5 <= int(x) <= 10:
        result.append(x)

with open(s, "w") as f:
    f.write(" ".join(result))