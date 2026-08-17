filename = input("Fayl nomi: ")

with open(filename, "r") as f:
    text = f.read()

characters = len(text.replace("\n", ""))
lines = len(text.splitlines())

print("Belgilar soni:", characters)
print("Qatorlar soni:", lines)