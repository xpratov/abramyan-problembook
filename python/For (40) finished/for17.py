a = float(input("A - haqiqiy sonini kiriting: "))
n = int(input("N - butun sonini kiriting: "))

summa=0

for i in range(n+1):
  summa+=a**i

print(summa)