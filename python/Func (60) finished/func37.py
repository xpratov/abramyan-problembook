import math as m

def Power1(a, b):
  if a<=0:
    return 0
  return m.exp(b*(m.log(a)))

P = float(input("P ni kiriting: "))
A = float(input("A ni kiriting: "))
B = float(input("B ni kiriting: "))
C = float(input("C ni kiriting: "))

# Darajalarni hisoblash
resA = Power1(A, P)
resB = Power1(B, P)
resC = Power1(C, P)

# Natijalarni chiqarish
print(f"A^P = {resA}")
print(f"B^P = {resB}")
print(f"C^P = {resC}")

