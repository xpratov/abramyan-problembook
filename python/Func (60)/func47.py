def GCD2(A, B):
    A, B = abs(A), abs(B)
    while B != 0:
        A, B = B, A % B
    return A

def Frac1(a, b):
    if b == 0:
        raise ValueError("Mahraj nolga teng bo'lishi mumkin emas!")
    
    common = GCD2(a, b)
    p = a // common
    q = b // common
    if q < 0:
        p = -p
        q = -q
        
    return p, q

def add_fractions(a, b, c, d):
    new_numerator = a * d + c * b
    new_denominator = b * d
    return Frac1(new_numerator, new_denominator)

try:
    print("Sonlarni kiriting:")
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    d = int(input("d = "))
    e = int(input("e = "))
    f = int(input("f = "))
    g = int(input("g = "))
    h = int(input("h = "))

    pairs = [
        ("a/b + c/d", a, b, c, d),
        ("a/b + e/f", a, b, e, f),
        ("a/b + g/h", a, b, g, h)
    ]

    print("\nNatijalar (qisqarmas ko'rinishda):")
    print("-" * 40)
    for label, n1, d1, n2, d2 in pairs:
        p, q = add_fractions(n1, d1, n2, d2)
        print(f"{label} natijasi: {p}/{q}")

except ValueError as err:
    print(f"Xatolik: {err}")