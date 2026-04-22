n = int(input("N: "))
a = list(map(float, input().split()))

for i in range((n // 2) * 2 - 1, 0, -2):
    a.insert(i + 1, a[i])

print(a)