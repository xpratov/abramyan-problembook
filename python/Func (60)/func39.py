import math as m

def Power1(a, b):
  if a<=0:
    return 0
  return m.exp(b*(m.log(a)))

def Power2(a, n):
  if n==0:
    return 1
  result = 1.0
  for _ in range(abs(n)):
    result *= a
  if n<0:
    result = 1/result
  return result

def Power3(A, B):
    if B == int(B):
        return Power2(A, int(B))
    else:
        return Power1(A, B)

# Ma'lumotlarni kiritish
P = float(input("P ni kiriting: "))
A = float(input("A ni kiriting: "))
B = float(input("B ni kiriting: "))
C = float(input("C ni kiriting: "))

# Natijalarni hisoblash va chiqarish
print(f"A^P = {Power3(A, P)}")
print(f"B^P = {Power3(B, P)}")
print(f"C^P = {Power3(C, P)}")