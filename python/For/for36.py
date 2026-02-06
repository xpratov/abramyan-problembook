n, k = map(int, input("N, K - butun sonlarni kiriting: ").split())

summa = 0

for i in range(n+1):
  summa+= i**k

print(summa)