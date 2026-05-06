n = int(input("N - butun sonini kiriting: "))
a = list(map(float, input(f"{n} ta son kiriting: ").split()))

for i in range(0, n, 2):
  a[i], a[i+1] = a[i+1], a[i]

print(a)