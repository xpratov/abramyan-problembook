s0 = input("Yangi fayl nomi: ")
n = int(input("N (<=4): "))

with open(s0, "wb") as out:
    for i in range(n):
        s = input(f"{i+1}-fayl nomi: ")
        with open(s, "rb") as f:
            out.write(f.read())