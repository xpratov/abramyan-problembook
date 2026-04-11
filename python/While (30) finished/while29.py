eps = float(input("eps = "))

a1, a2 = 1.0, 2.0
k = 2

while abs(a2 - a1) >= eps:
    a1, a2 = a2, (a1 + 2*a2) / 3
    k += 1

print(f"K = {k}")
print(f"A(K-1) = {a1}")
print(f"A(K) = {a2}")