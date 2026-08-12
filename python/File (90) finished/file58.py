s = input("Binary fayl nomini kiriting: ")

with open(s, "rb") as f:
    data = f.read()

index = data.find(b' ')

data = data[:index]

with open("file.bin", "wb") as f:
    f.write(data)