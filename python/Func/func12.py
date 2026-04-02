
def IsPowerN(k, n):
  if k<=0 or n<=1: False
  while k%n==0:
    k = k//n
  return k==1

n_base = int(input("N asosini kiriting (N > 1): "))
count = 0

print("10 ta sonni kiriting:")
for i in range(10):
    num = int(input(f"{i+1}-son: "))
    if IsPowerN(num, n_base):
        count += 1

print(f"To'plamda {n_base} ning darajasi bo'lgan {count} ta son bor.")