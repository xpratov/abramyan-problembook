x = float(input("X - haqiqiy son (|X|<1)ni kiriting: "))
n = int(input("N - butun son (>0)ni kiriting: "))

summa=0
for index, i in enumerate(range(1, 2*n+2, 2)):
  summa+= (-1)**(index)*((x**i)/i)

print(summa)