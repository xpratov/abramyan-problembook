filename = input("Fayl nomi: ")

with open(filename, "r") as f:
    lines = f.readlines()

for i in range(len(lines)):
    line = lines[i].rstrip("\n")

    if line != "":
        spaces = len(line) - len(line.lstrip(" "))

        if spaces % 2 == 1:
            spaces -= 1

        line = line[spaces // 2:]

        lines[i] = line + "\n"

with open(filename, "w") as f:
    f.writelines(lines)