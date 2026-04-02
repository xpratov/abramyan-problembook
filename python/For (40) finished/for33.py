n = int(input("N sonini kiriting: "))

result = []

prev, then = 1, 1

for i in range(n+1):
  result.append(prev)
  prev, then = then, prev + then

print(*result)
