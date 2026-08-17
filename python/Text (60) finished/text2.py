filename = input("Fayl nomi: ")
N = int(input("N = "))

with open(filename, "w") as f:
    for i in range(1, N + 1):
        f.write("abcdefghijklmnopqrstuvwxyz"[:i] + "\n")