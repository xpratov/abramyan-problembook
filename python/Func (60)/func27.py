
def DigitCS(k):
  count = len(str(k))
  summa = 0
  for i in str(k):
    summa+=int(i)
  return count, summa

numbers = [23, 45, 6754, 21345, 654]

for i in numbers: 
  print(DigitCS(i))