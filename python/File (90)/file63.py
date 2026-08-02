k = int(input("K = "))
s = input("Asl fayl: ")
s1 = input("1-fayl: ")
s2 = input("2-fayl: ")

with open(s, "r") as f:
    data = f.read().splitlines()

with open(s1, "w") as f1, open(s2, "w") as f2:
    for line in data:
        if len(line) < k:
            f1.write(line + "\n")
            f2.write(" \n")
        else:
            f1.write(line[:k] + "\n")
            f2.write(line[k - 1] + "\n")