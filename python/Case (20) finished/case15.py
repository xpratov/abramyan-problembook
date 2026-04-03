N = int(input("Karta qiymatini kiriting (6-14): "))
M = int(input("Karta turini kiriting (1-4): "))

match N:
    case 6:  n_nomi = "olti"
    case 7:  n_nomi = "yetti"
    case 8:  n_nomi = "sakkiz"
    case 9:  n_nomi = "to'qqiz"
    case 10: n_nomi = "o'n"
    case 11: n_nomi = "valet"
    case 12: n_nomi = "dama"
    case 13: n_nomi = "qirol"
    case 14: n_nomi = "tuz"
    case _:  n_nomi = "noma'lum qiymat"

match M:
    case 1:  m_nomi = "pika"
    case 2:  m_nomi = "tref"
    case 3:  m_nomi = "g'ishtin"
    case 4:  m_nomi = "olma"
    case _:  m_nomi = "noma'lum tur"

if n_nomi != "noma'lum qiymat" and m_nomi != "noma'lum tur":
    print(f"{m_nomi} {n_nomi}si")
else:
    print("Xato ma'lumot kiritildi!")