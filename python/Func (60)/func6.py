def SumRange(a, b):
  if a>b:
    return 0
  summa=0
  for i in range(a, b+1):
    summa+=i
  return summa

a, b, c = map(int, input("A, B, C - butun sonlarni kiriting: ").split())

print(SumRange(a, b))
print(SumRange(b, c))
