n = int(input("N: "))
a = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

counts = {}
for x in a:
    counts[x] = counts.get(x, 0) + 1

write = 0
for read in range(n):
    if counts[a[read]] <= 2:
        a[write] = a[read]
        write += 1

del a[write:]

print(len(a))
print(*a)