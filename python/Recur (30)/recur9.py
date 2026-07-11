def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)


a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
d = int(input("D = "))

print("GCD(A, B) =", GCD(a, b))
print("GCD(A, C) =", GCD(a, c))
print("GCD(A, D) =", GCD(a, d))