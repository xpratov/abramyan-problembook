s = input("Fayl nomi: ")

with open(s, "r") as f:
    lines = f.readlines()

result = []

for line in lines:
    result.append(line)

    if line.strip() == "":
        result.append(line)

with open(s, "w") as f:
    f.writelines(result)