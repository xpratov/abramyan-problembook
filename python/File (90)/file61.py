s = input("Fayl nomini kiriting: ")

with open(s, "rb") as f:
    data = f.read()

index = data.rfind(b' ')

data = data[index + 1:]

with open(s, "wb") as f:
    f.write(data)