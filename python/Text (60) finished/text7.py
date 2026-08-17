filename = input("Fayl nomi: ")
S = input("S = ")

with open(filename, "r") as f:
    data = f.read()

with open(filename, "w") as f:
    f.write(S + data)