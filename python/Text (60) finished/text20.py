filename = input("Fayl nomi: ")

with open(filename, "r") as f:
    text = f.read()

while "  " in text:
    text = text.replace("  ", " ")

with open(filename, "w") as f:
    f.write(text)