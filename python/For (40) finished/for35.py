n = int(input("N - butun sonini kiriting: "))

result = []
a1, a2, a3 = 1, 2, 3

for i in range(n+1):
  result.append(a1)
  a1, a2, a3 = a2, a3, (a3 + a2 - 2*a1)

print(*result)