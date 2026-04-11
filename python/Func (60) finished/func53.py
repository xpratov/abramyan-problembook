def MonthDays(m, y):
    if m in [4, 6, 9, 11]:
        return 30
    elif m == 2:
        return 29 if IsLeapYear(y) else 28
    else:
        return 31

y = int(input("Yilni kiriting: "))
m1, m2, m3 = 2, 4, 12 

for m in [m1, m2, m3]:
    print(f"{y}-yil {m}-oyda {MonthDays(m, y)} kun bor.")