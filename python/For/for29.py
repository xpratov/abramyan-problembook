n = int(input("N - butun sonni kiriting: "))
a, b = map(float, input("A, B - haqiqiy sonlarni kiriting: ").split())

h = (b-a) / n
result = []

for i in range(1, n+1):
  current = a + i*h
  result.append(current)

print(h)
print(*result)