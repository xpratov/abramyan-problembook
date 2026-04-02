x = float(input("X - haqiqiy son (|X|<1)ni kiriting: "))
n = int(input("N - butun son (>0)ni kiriting: "))

summa=0
for i in range(1, n+1):
  summa+= (-1)**(i-1)*((x**i)/i)

print(summa)