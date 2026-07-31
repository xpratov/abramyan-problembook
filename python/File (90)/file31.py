s = input("Fayl nomini kiriting: ")

with open(s, "r") as f:
    components = f.read().split()

components = components[-50:]

with open(s, "w") as f:
    f.write(" ".join(components))