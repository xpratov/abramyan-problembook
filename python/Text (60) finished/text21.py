filename = input("Fayl nomi: ")

with open(filename, "r") as f:
    lines = f.readlines()

lines = lines[:-3]

with open(filename, "w") as f:
    f.writelines(lines)