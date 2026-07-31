s = input("Fayl nomini kiriting: ")

with open(s, "r") as f:
    components = f.read().split()

half = len(components) // 2
components = components[half:]

with open(s, "w") as f:
    f.write(" ".join(components))