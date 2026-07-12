n = int(input("N - butun sonini kiriting: "))
nlar = list(map(float, input("N ta haqiqiy son kiriting: ").split()))

revs = nlar[::-1]

first_zero = revs.index(0)
second_zero = revs.index(0, first_zero+1)

summa = 0
for i in range(first_zero+1, second_zero):
  summa += revs[i]

print(summa)

