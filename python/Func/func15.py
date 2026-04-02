
def DigitN(k, n):
  if len(str(k))<n: return -1
  k = str(k)[::-1]
  return k[n-1]

numbers = [235, 23465, 5646, 2346, 476573524]
for i in range(len(numbers)):
  print(DigitN(numbers[i], 1))
  print(DigitN(numbers[i], 2))
  print(DigitN(numbers[i], 3))
  print(DigitN(numbers[i], 4))
  print(DigitN(numbers[i], 5))