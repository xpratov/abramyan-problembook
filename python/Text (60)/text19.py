filename = input("Fayl nomi: ")

with open(filename, "r") as f:
    text = f.read()

text = text.swapcase()

with open(filename, "w") as f:
    f.write(text)