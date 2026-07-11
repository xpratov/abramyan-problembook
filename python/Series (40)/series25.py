n = int(input("N - butun sonini kiriting: "))
nlar = list(map(int, input("N ta haqiqiy son kiriting: ").split()))

first_zero = nlar.index(0)
last_zero = nlar.rindex(0)

summa = 0
for i in range(first_zero+1, last_zero):
  summa += nlar[i]

print(summa)