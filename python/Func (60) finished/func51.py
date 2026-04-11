def IncTime(H, M, S, T):
    total_seconds = S + T
    
    S = total_seconds % 60
    extra_minutes = total_seconds // 60
    
    total_minutes = M + extra_minutes
    M = total_minutes % 60
    extra_hours = total_minutes // 60
    H = H + extra_hours
    
    return H, M, S

try:
    h = int(input("H (soat) = "))
    m = int(input("M (daqiqa) = "))
    s = int(input("S (soniya) = "))
    t = int(input("T (qo'shiladigan soniya) = "))

    h_new, m_new, s_new = IncTime(h, m, s, t)

    print(f"\nYangi vaqt: {h_new} soat, {m_new} daqiqa, {s_new} soniya")
    print(f"Formatlangan: {h_new:02}:{m_new:02}:{s_new:02}")

except ValueError:
    print("Iltimos, faqat butun son kiriting!")