n = int(input("N: "))
a = list(map(int, input(f"{n} ta butun son kiriting: ").split()))

seen = set()
write_idx = n - 1

for read_idx in range(n - 1, -1, -1):
    if a[read_idx] not in seen:
        seen.add(a[read_idx])
        a[write_idx] = a[read_idx]
        write_idx -= 1

del a[:write_idx + 1]

print(len(a))
print(*a)