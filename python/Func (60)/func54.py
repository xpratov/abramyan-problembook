def PrevDate(d, m, y):
    if d > 1:
        return d - 1, m, y
    else:
        if m > 1:
            new_m = m - 1
            new_d = MonthDays(new_m, y)
            return new_d, new_m, y
        else:
            return 31, 12, y - 1

dates = [(1, 1, 2024), (1, 3, 2024), (15, 5, 2023)]
for d, m, y in dates:
    pd, pm, py = PrevDate(d, m, y)
    print(f"{d}.{m}.{y} -> Oldingi sana: {pd}.{pm}.{py}")