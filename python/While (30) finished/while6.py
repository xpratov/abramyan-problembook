n = int(input("N - butun sonini kiriting: "))

result = 1.0
while n>0:
  result *= n
  n -= 2

print(result)