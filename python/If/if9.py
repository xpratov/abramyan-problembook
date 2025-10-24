a, b = map(float, input("Ikkita haqiqiy son kiriting: ").split())

if a>b:
  a, b = b, a

print(a, b)