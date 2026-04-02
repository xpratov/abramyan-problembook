a, b = map(int, input("Ikkita butun son kiriting: ").split())

s=a+b

if a!=b:
  a, b = s, s
else:
  a, b = 0, 0

print(a, b)