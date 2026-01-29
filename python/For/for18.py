a = float(input("A - haqiqiy sonini kiriting: "))
n = int(input("N - butun sonini kiriting: "))

summa = 1

for i in range(1, n+1):
  summa+=((-1)**i)*(a**i)

print(summa)