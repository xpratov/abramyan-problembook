def GCD2(A, B):
    while B != 0:
        A, B = B, A % B
    return A

def GCD3(A, B, C):
    vaqtinchalik_ekub = GCD2(A, B)
    yakuniy_ekub = GCD2(vaqtinchalik_ekub, C)
    return yakuniy_ekub

try:
    print("\nTo'rtta butun sonni kiriting (A, B, C, D):")
    A = int(input("A = "))
    B = int(input("B = "))
    C = int(input("C = "))
    D = int(input("D = "))

    print("\nUchta son uchun EKUB (GCD3) natijalari:")
    print(f"GCD3({A}, {B}, {C}) = {GCD3(A, B, C)}")
    print(f"GCD3({A}, {C}, {D}) = {GCD3(A, C, D)}")
    print(f"GCD3({B}, {C}, {D}) = {GCD3(B, C, D)}")

except ValueError:
    print("Iltimos, butun son kiriting!")