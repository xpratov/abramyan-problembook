def AddLeftDigit(d, k):
  n = len(str(k))
  return d*(10**n) + k

K = int(input("K sonini kiriting: "))
D1 = int(input("D1 raqamini kiriting: "))
D2 = int(input("D2 raqamini kiriting: "))

K = AddLeftDigit(D1, K)
print(f"D1 qo'shilgandan keyin: {K}")

K = AddLeftDigit(D2, K)
print(f"D2 qo'shilgandan keyin: {K}")