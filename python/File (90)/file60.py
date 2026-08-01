filename = input("Fayl nomi: ")

with open(filename, "rb") as f:
    data = f.read()

index = data.find(b' ')

data = data[index + 1:]

with open(filename, "wb") as f:
    f.write(data)

print("Natija saqlandi.")