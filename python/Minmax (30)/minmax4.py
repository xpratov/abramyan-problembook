n = int(input("N - haqiqiy sonlar sonini kiriting: "))
realn = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

minn=realn[0]

for i in range(n):
  if minn>realn[i]:
    minn=i

print(minn)