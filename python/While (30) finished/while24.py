n = int(input("N = "))

f1, f2 = 1, 1
while f2 < n:
    f1, f2 = f2, f1 + f2

print(f2 == n)