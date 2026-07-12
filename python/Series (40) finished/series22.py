n = int(input("N - butun sonini kiriting: "))
nlar = list(map(float, input("N ta haqiqiy son kiriting: ").split()))

result = 0
for i in range(n-1):
  if nlar[i]<=nlar[i+1]:
    result = i
    break

print(result+2)