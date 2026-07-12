n = int(input("N - butun sonini kiriting: "))
nlar = list(map(float, input("N ta haqiqiy son kiriting: ").split()))

result = True
for i in range(n-1):
    if nlar[i]<nlar[i+1]:
      continue
    result = False
    break

print(result)

