x = float(input("X - haqiqiy sonini kiriting: "))
n = int(input("N - butun sonini kiriting: "))

result = 0

def factorial(n):
  k = 1
  for i in range(1, n+1):
    k*=i
  return k

ishora = 1
for i in range(1, 2*n+2, 2):
  result += (x**i/factorial(i))*ishora
  ishora*=-1

print(result)

