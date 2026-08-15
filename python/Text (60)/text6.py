file1 = input("1-fayl: ")
file2 = input("2-fayl: ")

with open(file2, "r") as f:
    data = f.read()

with open(file1, "a") as f:
    f.write(data)