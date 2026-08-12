s = input("Fayl nomini kiriting: ")

with open(s, "r") as f:
    components = list(map(int, f.read().split()))

result = []

for x in components:
    if x > 0:
        result.extend(["0", "0", "0"])
    else:
        result.append(str(x))

with open(s, "w") as f:
    f.write(" ".join(result))