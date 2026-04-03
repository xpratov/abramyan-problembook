import math

n = int(input("Element tartib raqamini kiriting (1-4): "))
val = float(input("Element qiymatini kiriting: "))

match n:
    case 1: 
        a = val
        c = a * math.sqrt(2)
        h = c / 2
        s = c * h / 2
    case 2: 
        c = val
        a = c / math.sqrt(2)
        h = c / 2
        s = c * h / 2
    case 3: 
        h = val
        c = 2 * h
        a = c / math.sqrt(2)
        s = c * h / 2
    case 4: 
        s = val
        c = math.sqrt(4 * s)
        h = c / 2
        a = c / math.sqrt(2)
    case _: 
        print("Xato! Faqat 1-4 oralig'idagi raqam kiriting.")
        a = c = h = s = None

if a is not None:
    print(f"1) Katet a = {a:.2f}")
    print(f"2) Gipotenuza c = {c:.2f}")
    print(f"3) Balandlik h = {h:.2f}")
    print(f"4) Yuza S = {s:.2f}")