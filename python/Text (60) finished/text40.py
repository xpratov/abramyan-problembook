file1 = input("1-fayl nomi: ")
file2 = input("2-fayl nomi: ")
file3 = input("Natijaviy fayl nomi: ")

with open(file1, "r") as f:
    numbers1 = f.read().split()

with open(file2, "r") as f:
    numbers2 = f.read().split()


with open(file3, "w") as f:
    for i in range(len(numbers1)):
        f.write("|")
        f.write(numbers1[i].rjust(30))
        f.write("|")
        f.write(numbers2[i].rjust(30))
        f.write("|\n")