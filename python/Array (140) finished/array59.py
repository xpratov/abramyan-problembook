n = int(input("N - butun sonini kiriting: "))
a = list(map(float, input(f"{n} ta haqiqiy son kiriting: ").split()))

bksum = 0
b = []

for i in range(n):
  bksum += a[i]
  b.append(bksum/(i+1))

print(b)