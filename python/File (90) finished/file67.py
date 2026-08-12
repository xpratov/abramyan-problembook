s = input("Asl fayl: ")
s1 = input("Kunlar fayli: ")
s2 = input("Oylar fayli: ")

with open(s, "r") as f:
    data = f.read().splitlines()

with open(s1, "w") as f1, open(s2, "w") as f2:
    for line in data:
        day, month, year = line.split("/")
        f1.write(day + "\n")
        f2.write(month + "\n")