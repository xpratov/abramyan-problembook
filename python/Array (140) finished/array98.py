n = int(input("N: "))
a = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

counts = {}
for x in a:
    counts[x] = counts.get(x, 0) + 1

write_idx = 0
for read_idx in range(n):
    if counts[a[read_idx]] >= 3:
        a[write_idx] = a[read_idx]
        write_idx += 1

del a[write_idx:]

print(len(a))
print(*a)