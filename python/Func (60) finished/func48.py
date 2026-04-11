def GCD2(A, B):
    while B != 0:
        A, B = B, A % B
    return A

def LCM2(A, B):
    if A == 0 or B == 0:
        return 0
    return abs(A * B) // GCD2(A, B)

try:
    print("To'rtta butun sonni kiriting (A, B, C, D):")
    A = int(input("A = "))
    B = int(input("B = "))
    C = int(input("C = "))
    D = int(input("D = "))

    print("\nEKUK (LCM) natijalari:")
    print(f"LCM2({A}, {B}) = {LCM2(A, B)}")
    print(f"LCM2({A}, {C}) = {LCM2(A, C)}")
    print(f"LCM2({A}, {D}) = {LCM2(A, D)}")

except ValueError:
    print("Iltimos, butun son kiriting!")