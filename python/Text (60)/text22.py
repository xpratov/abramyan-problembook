K = int(input("K = "))
filename = input("Fayl nomi: ")

with open(filename, "r") as f:
    lines = f.readlines()

lines = lines[:-K]

with open(filename, "w") as f:
    f.writelines(lines)