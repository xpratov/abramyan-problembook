n = int(input("N: "))
a = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

write = 1

for read in range(1, n):
  if a[read] != a[read-1]:
    a[write] = a[read]
    write+=1

del a[write:]  

print(len(a), a)