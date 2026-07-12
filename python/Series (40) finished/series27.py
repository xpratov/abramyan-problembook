n = int(input("N - butun sonini kiriting: "))
nlar = list(map(float, input("N ta haqiqiy son kiriting: ").split()))

for i in range(n):
  print(nlar[i]**(i+1))

