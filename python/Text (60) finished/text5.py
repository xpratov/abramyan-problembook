filename = input("Fayl nomi: ")
S = input("S = ")

with open(filename, "a") as f:
    f.write(S)