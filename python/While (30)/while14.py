a = float(input("A - haqiqiy sonini kiriting: "))

k = 0
summa = 0

while summa + 1/(k+1) < a:
  k += 1
  summa += 1/k

print(k, summa)