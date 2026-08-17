K = int(input("K = "))
filename = input("Fayl nomi: ")

with open(filename, "r") as f:
    lines = f.readlines()

if 1 <= K <= len(lines):
    lines.pop(K - 1)

    with open(filename, "w") as f:
        f.writelines(lines)