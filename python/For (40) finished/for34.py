n = int(input("N sonini kiriting: "))

result = []

prev, then = 1, 2

for i in range(n+1):
  result.append(prev)
  prev, then = then, (prev + 2*then)/3

print(*result)
