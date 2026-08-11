def LeapYear(D):
    return D["Year"] % 4 == 0 and (
        D["Year"] % 100 != 0 or D["Year"] % 400 == 0
    )


for _ in range(5):
    day, month, year = map(int, input().split())

    D = {
        "Day": day,
        "Month": month,
        "Year": year
    }

    print(LeapYear(D))