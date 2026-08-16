file1 = input("1-fayl: ")
file2 = input("2-fayl: ")

with open(file1, "r") as f:
    lines1 = f.readlines()

with open(file2, "r") as f:
    lines2 = f.readlines()

for i in range(min(len(lines1), len(lines2))):
    lines1[i] = lines1[i].rstrip("\n") + lines2[i]

with open(file1, "w") as f:
    f.writelines(lines1)