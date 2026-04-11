n = int(input("N - butun sonini kiriting: "))

count = 0
summa = 0

while n>0:
  summa += n%10
  n //= 10
  count += 1

print(count, summa)