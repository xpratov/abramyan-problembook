s = input("Fayl nomini kiriting: ")

with open(s, "r") as f:
    dates = f.read().split()

earliest = None

for date in dates:
    day, month, year = map(int, date.split("/"))

    if month in (3, 4, 5):
        if earliest is None:
            earliest = date
        else:
            d1, m1, y1 = map(int, earliest.split("/"))
            if (year, month, day) < (y1, m1, d1):
                earliest = date

print(earliest if earliest else "")