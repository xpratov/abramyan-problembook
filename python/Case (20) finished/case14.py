import math

n = int(input("Element tartib raqamini kiriting (1-4): "))
val = float(input("Element qiymatini kiriting: "))

match n:
    case 1: 
        a = val
        r1 = a * math.sqrt(3) / 6
        r2 = 2 * r1
        s = (a**2) * math.sqrt(3) / 4
    case 2: 
        r1 = val
        a = r1 * 6 / math.sqrt(3)
        r2 = 2 * r1
        s = (a**2) * math.sqrt(3) / 4
    case 3: 
        r2 = val
        r1 = r2 / 2
        a = r1 * 6 / math.sqrt(3)
        s = (a**2) * math.sqrt(3) / 4
    case 4:
        s = val
        a = math.sqrt(4 * s / math.sqrt(3))
        r1 = a * math.sqrt(3) / 6
        r2 = 2 * r1
    case _:
        print("Xato! Faqat 1 dan 4 gacha raqam kiriting.")
        a = r1 = r2 = s = None

if a is not None:
    print(f"1) Tomon a = {a:.2f}")
    print(f"2) Ichki chizilgan aylana radiusi R1 = {r1:.2f}")
    print(f"3) Tashqi chizilgan aylana radiusi R2 = {r2:.2f}")
    print(f"4) Yuza S = {s:.2f}")