s1 = input("Asl fayl nomini kiriting: ")
s2 = input("Yangi fayl nomini kiriting: ")

with open(s1, "r") as f:
    dates = f.read().split()

dates.sort(key=lambda x: tuple(map(int, x.split("/")))[::-1], reverse=True)

with open(s2, "w") as f:
    f.write("\n".join(dates))