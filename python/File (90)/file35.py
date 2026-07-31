s = input("Fayl nomini kiriting: ")

with open(s, "r") as f:
    components = f.read().split()

components = ["0"] * (50 - len(components)) + components

with open(s, "w") as f:
    f.write(" ".join(components))