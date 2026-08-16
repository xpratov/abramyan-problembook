S = input("S = ")
filename = input("Fayl nomi: ")

with open(filename, "r") as f:
    lines = f.readlines()

for i in range(len(lines)):
    if lines[i].strip() == "":
        lines[i] = S + "\n"

with open(filename, "w") as f:
    f.writelines(lines)