s = input("Asl fayl: ")
t = input("Yangi fayl: ")

with open(s, "r") as f:
    data = f.read().splitlines()

data.sort()

with open(t, "w") as f:
    for line in data:
        f.write(line + "\n")