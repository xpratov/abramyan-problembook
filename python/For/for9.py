import math as m

a, b = map(int, input("a, b - butun sonlarni kiriting: ").split())

total=0
for i in range(a, b):
  total+=m.sqrt(i)

print("a dan b gacha butun sonlar ildizlarining yig'indisi - ", total)