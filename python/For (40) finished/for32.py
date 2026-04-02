n = int(input("N - butun sonini kiriting: "))

prev = 1
result = []

for i in range(1, n+1):
  el = (prev + 1) / i
  result.append(el)
  prev = el

print(*result)



