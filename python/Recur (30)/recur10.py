k = int(input("K - butun sonini kiriting: "))

def DigitSum(k):
  if k==0:
    return 0
  return k%10 + DigitSum(k//10)

summa = DigitSum(k)
print(summa)