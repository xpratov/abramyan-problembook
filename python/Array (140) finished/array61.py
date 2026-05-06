n = int(input("N - butun sonini kiriting: "))
a = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

b = []
summa = sum(a)

for i in range(n):
  b.append(summa/(n-i))
  summa -= a[i]

print(b)