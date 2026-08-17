filename = input("Fayl nomi: ")
N = int(input("N = "))
K = int(input("K = "))

with open(filename, "w") as f:
    for _ in range(N):
        f.write("*" * K + "\n")