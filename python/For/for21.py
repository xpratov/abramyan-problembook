n = int(input("N - butun sonini kiriting: "))

fact=float(1)
summa=float(1)

for i in range(1, n+1):
  fact*=i
  summa+=(1/fact)

print(summa) # Matematikadagi e konstantasining kelib chiqishi!