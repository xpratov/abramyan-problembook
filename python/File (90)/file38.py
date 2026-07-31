s = input("Fayl nomini kiriting: ")

with open(s, "r") as f:
    components = f.read().split()

result = []

for i in range(len(components)):
    result.append(components[i])
    if i % 2 == 0:
        result.append(components[i])

with open(s, "w") as f:
    f.write(" ".join(result))