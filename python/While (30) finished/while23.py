a = int(input("A = "))
b = int(input("B = "))

while b != 0:
    a, b = b, a % b

print("EKUB:", a)