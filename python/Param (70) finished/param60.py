def LeapYear(D):
    return D["Year"] % 4 == 0 and (
        D["Year"] % 100 != 0 or D["Year"] % 400 == 0
    )


def DaysInMonth(D):
    if D["Month"] == 2:
        if LeapYear(D):
            return 29
        return 28

    if D["Month"] in (4, 6, 9, 11):
        return 30

    return 31


for _ in range(5):
    day, month, year = map(int, input().split())

    D = {
        "Day": day,
        "Month": month,
        "Year": year
    }

    print(DaysInMonth(D))