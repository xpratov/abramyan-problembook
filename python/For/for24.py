x = float(input("x="))
n = int(input("n="))

def factorial(n):
  result = 1
  for i in range(1, n+1):
    result*=i
  return result
  
summa = 0
for i in range(0, n+1):
  current = (-1)**i * x**(2*i)/factorial(2*i)
  summa+=current

print(summa)