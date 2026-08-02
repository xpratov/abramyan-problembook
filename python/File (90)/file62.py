s = input("Fayl nomini kiriting: ")

with open(s, "rb") as f:
    data = f.read()

data = bytes(sorted(data))

with open(s, "wb") as f:
    f.write(data)