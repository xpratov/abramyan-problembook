def IsLeapYear(y):
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

years = [2000, 2024, 1900, 2023, 2100]
for y in years:
    print(f"{y}-yil kabisami? {IsLeapYear(y)}")