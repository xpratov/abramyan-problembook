s = input("Asl fayl: ")
t = input("Yangi fayl: ")

with open(s, "r") as f:
    data = f.read().splitlines()

mx = max(len(line) for line in data)

with open(t, "w") as f:
    for line in reversed(data):
        if len(line) == mx:
            f.write(line + "\n")