a, b = map(int, input("a, b - butun sonlarni kiriting: ").split())

for i in range(b-1, a, -1):
  print(i)
print(abs(a-b)-1)