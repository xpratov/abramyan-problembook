n = int(input("N - butun sonini kiriting: "))

summa = 0

for i in range(n+1):
  summa += i**i

print(summa)