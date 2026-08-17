file1 = input("1-fayl: ")
file2 = input("2-fayl: ")

with open(file1, "r") as f:
    data1 = f.read()

with open(file2, "r") as f:
    data2 = f.read()

with open(file1, "w") as f:
    f.write(data2 + data1)