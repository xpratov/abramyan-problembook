n = int(input("N - butun sonini kiriting: "))
a = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

b = []
for i in range(n):
  if a[i]%2==0:
    b.append(a[i])

print(len(b), b)
