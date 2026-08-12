s = input("Asl fayl: ")
s1 = input("Oylar fayli: ")
s2 = input("Yillar fayli: ")

with open(s, "r") as f:
    data = f.read().splitlines()

with open(s1, "w") as f1, open(s2, "w") as f2:
    for line in reversed(data):
        day, month, year = line.split("/")
        f1.write(month + "\n")
        f2.write(year + "\n")