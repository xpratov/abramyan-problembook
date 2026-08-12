s = input("Fayl nomini kiriting: ")

with open(s, "r") as f:
    components = f.read().split()

result = []

for i in range(len(components)):
    if (i + 1) % 2 == 0:
        result.extend(["0", "0"])
    else:
        result.append(components[i])

with open(s, "w") as f:
    f.write(" ".join(result))