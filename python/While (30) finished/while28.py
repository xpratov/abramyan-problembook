eps = float(input("eps = "))

a_prev = 2
a_curr = 2 + 1/a_prev
k = 2

while abs(a_curr - a_prev) >= eps:
    a_prev = a_curr
    a_curr = 2 + 1/a_prev
    k += 1

print(f"K = {k}")
print(f"A(K-1) = {a_prev}")
print(f"A(K) = {a_curr}")