def NextDate(d, m, y):
    days_in_month = MonthDays(m, y)
    
    if d < days_in_month:
        return d + 1, m, y
    else:
        if m < 12:
            return 1, m + 1, y
        else:
            return 1, 1, y + 1

dates = [(31, 12, 2023), (28, 2, 2024), (30, 4, 2023)]
for d, m, y in dates:
    nd, nm, ny = NextDate(d, m, y)
    print(f"{d}.{m}.{y} -> Keyingi sana: {nd}.{nm}.{ny}")