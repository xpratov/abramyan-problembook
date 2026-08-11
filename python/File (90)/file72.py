s = input("Fayl nomini kiriting: ")

with open(s, "r") as f:
    dates = f.read().split()

latest = None

for date in dates:
    day, month, year = map(int, date.split("/"))

    if month in (9, 10, 11):
        if latest is None:
            latest = date
        else:
            d1, m1, y1 = map(int, latest.split("/"))
            if (year, month, day) > (y1, m1, d1):
                latest = date

print(latest if latest else "")