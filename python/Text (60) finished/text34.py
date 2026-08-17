filename = input("Fayl nomi: ")

with open(filename, "r") as f:
    lines = f.readlines()

for i in range(len(lines)):
    line = lines[i].rstrip("\n")

    if line != "":
        spaces = 50 - len(line)
        lines[i] = " " * spaces + line + "\n"

with open(filename, "w") as f:
    f.writelines(lines)