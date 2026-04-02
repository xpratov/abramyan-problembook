x = float(input("X - haqiqiy sonini kiriting: "))
n = int(input("N - butun sonini kiriting: "))

fact=1
result=1

for i in range(1, n+1):
  fact*=i
  result+=(x**i/fact)

print(result)
