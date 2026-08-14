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

    # Oy noto'g'ri
    if month < 1 or month > 12:
        return 1

    # Kun noto'g'ri
    if day < 1 or day > DaysInMonth(month, year):
        return 2

    return 0


dates = [
    (15, 8, 2026),
    (31, 4, 2026),
    (29, 2, 2024),
    (29, 2, 2023),
    (10, 13, 2026)
]

for D in dates:
    print(CheckDate(D))