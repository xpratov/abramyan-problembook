p = float(input("P - haqiqiy sonini kiriting: "))

distant = 10
summa = 10
k=1

while distant<=200:
  k += 1
  distant += distant*p/100
  summa += distant

print(k, summa)