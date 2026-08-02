s = input("Asl fayl: ")
t = input("Yangi fayl: ")

with open(s, "r") as f:
    data = f.read().splitlines()

with open(t, "w") as f:
    for line in data:
        day, month, year = line.split("/")
        if int(month) in (6, 7, 8):
            f.write(line + "\n")