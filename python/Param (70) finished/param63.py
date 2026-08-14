def DaysInMonth(month, year):
    if month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return 29
        return 28

    if month in (4, 6, 9, 11):
        return 30

    return 31


def CheckDate(D):
    day, month, year = D

    if month < 1 or month > 12:
        return 1

    if day < 1 or day > DaysInMonth(month, year):
        return 2

    return 0


def NextDate(D):
    # Sana noto'g'ri bo'lsa, o'zgartirmaymiz
    if CheckDate(D) != 0:
        return

    if D[0] < DaysInMonth(D[1], D[2]):
        D[0] += 1

    else:
        D[0] = 1

        if D[1] < 12:
            D[1] += 1
        else:
            D[1] = 1
            D[2] += 1


dates = [
    [15, 8, 2026],
    [31, 7, 2026],
    [31, 12, 2026],
    [29, 2, 2024],
    [31, 4, 2026]
]

for D in dates:
    NextDate(D)
    print(D)