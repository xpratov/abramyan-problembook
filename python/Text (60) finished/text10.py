filename = input("Fayl nomi: ")
K = int(input("K = "))

with open(filename, "r") as f:
    lines = f.readlines()

if 1 <= K <= len(lines):
    lines.insert(K, "\n")

    with open(filename, "w") as f:
        f.writelines(lines)