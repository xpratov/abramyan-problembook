n = int(input("N - butun sonini kiriting: "))
a = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

def MinElem(a, n):
  minimum = a[0]
  for i in range(1, n):
    if a[i]<minimum:
      minimum = a[i]
  return minimum

print(MinElem(a, n))