n = int(input("N - butun sonini kiriting: "))

prev = 2
result = []

for i in range(n+1):
  el = 2 + 1/prev
  result.append(el)
  prev = el

print(*result)



