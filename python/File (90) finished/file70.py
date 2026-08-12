s = input("Asl fayl: ")
t = input("Yangi fayl: ")

with open(s, "r") as f:
    data = f.read().splitlines()

with open(t, "w") as f:
    for line in data:
        day, month, year = line.split("/")
        if int(month) in (12, 1, 2):
            f.write(line + "\n")