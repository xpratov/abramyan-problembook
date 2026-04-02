n = int(input("N - butun sonini kiriting: "))

fact=float(1)
summa=float(0)

for i in range(1, n+1):
  fact*=i
  summa+=fact

print(summa)