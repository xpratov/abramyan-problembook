def GCD2(A, B):
    while B != 0:
        A, B = B, A % B
    return A

try:
    A = int(input("A ni kiriting: "))
    B = int(input("B ni kiriting: "))
    C = int(input("C ni kiriting: "))
    D = int(input("D ni kiriting: "))

    print("\nNatijalar:")
    print(f"GCD2({A}, {B}) = {GCD2(A, B)}")
    print(f"GCD2({A}, {C}) = {GCD2(A, C)}")
    print(f"GCD2({A}, {D}) = {GCD2(A, D)}")

except ValueError:
    print("Iltimos, faqat butun sonlarni kiriting!")