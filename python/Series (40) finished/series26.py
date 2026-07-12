k, n = map(int, input("K va N butun sonlarni kiriting: ").split())
nlar = list(map(float, input("N ta haqiqiy son kiriting: ").split()))

for i in nlar:
  print(i**k)