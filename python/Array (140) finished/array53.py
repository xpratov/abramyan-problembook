n = int(input("N - butun sonini kiriting: "))
a = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))
b = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

c = []
for i in range(n):
  if a[i]>b[i]:
    c.append(a[i])
  else:
    c.append(b[i])

print(c)