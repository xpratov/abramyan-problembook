n = int(input("N: "))
a = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

seen = []
write = 0

for read in range(n):
  if a[read] not in seen:
    seen.append(a[read])
    a[write] = a[read]
    write+=1

del a[write:]

print(len(a), a)