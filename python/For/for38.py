n = int(input("N - butun sonini kiriting: "))

num = n
summa = 0

for i in range(n+1):
  summa += i**num
  num -= 1

print(summa)