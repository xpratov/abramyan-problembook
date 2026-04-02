a, b = map(int, input("a, b - butun sonlarni kiriting: ").split())

total=0
for i in range(a, b):
  total+=i

print("a dan b gacha butun sonlar yig'indisi - ", total)