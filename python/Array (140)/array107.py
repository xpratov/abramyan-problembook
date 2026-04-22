n = int(input("N: "))
a = list(map(float, input().split()))

start_idx = (n - 1) if (n - 1) % 2 == 0 else (n - 2)

for i in range(start_idx, -1, -2):
    a.insert(i + 1, a[i])
    a.insert(i + 1, a[i])

print(a)