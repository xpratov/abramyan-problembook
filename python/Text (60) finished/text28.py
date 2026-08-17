filename = input("Fayl nomi: ")

with open(filename, "r") as f:
    lines = f.readlines()

result = []

for line in lines:
    if line.startswith("     ") and result:
        result.append("\n")

    result.append(line)

with open(filename, "w") as f:
    f.writelines(result)