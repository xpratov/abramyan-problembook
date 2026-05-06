n = int(input("N - butun sonini kiriting: "))
a = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

b = []

for i in range(n):
  if a[i]<5:
    b.append(2*a[i])
  else:
    b.append(a[i]/2)

print(b)
