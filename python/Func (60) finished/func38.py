
def Power2(a, n):
  if n==0:
    return 1
  result = 1.0
  for _ in range(abs(n)):
    result *= a
  if n<0:
    result = 1/result
  return result

# Ma'lumotlarni kiritish
A = float(input("A (haqiqiy son) ni kiriting: "))
K = int(input("K (butun son) ni kiriting: "))
L = int(input("L (butun son) ni kiriting: "))
M = int(input("M (butun son) ni kiriting: "))

# Funksiyani chaqirish va natijalarni chiqarish
print(f"A^K = {Power2(A, K)}")
print(f"A^L = {Power2(A, L)}")
print(f"A^M = {Power2(A, M)}")