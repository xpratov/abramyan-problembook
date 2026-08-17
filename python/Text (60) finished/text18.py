K = int(input("K = "))
filename = input("Fayl nomi: ")

with open(filename, "r") as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i][K:]

with open(filename, "w") as f:
    f.writelines(lines)