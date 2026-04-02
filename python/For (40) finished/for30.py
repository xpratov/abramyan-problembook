import math as m
n = int(input("N - butun sonini kiriting: "))
a, b = map(float, input("A, B - haqiqiy sonlarni kiriting: ").split())

h = (b-a)/n
fx = []

for i in range(int(h)+1):
  current = 1-m.sin(a+i*h)
  fx.append(current)

print(h)
print(*fx)

