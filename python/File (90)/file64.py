s = input("Asl fayl: ")
t = input("Yangi fayl: ")

with open(s, "r") as f:
    data = f.read().splitlines()

mn = min(len(line) for line in data)

with open(t, "w") as f:
    for line in data:
        if len(line) == mn:
            f.write(line + "\n")