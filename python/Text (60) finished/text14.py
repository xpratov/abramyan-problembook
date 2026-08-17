filename = input("Fayl nomi: ")

with open(filename, "r") as f:
    lines = f.readlines()

lines.pop()

with open(filename, "w") as f:
    f.writelines(lines)