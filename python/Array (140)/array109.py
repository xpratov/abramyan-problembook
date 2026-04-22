n = int(input("N: "))
a = list(map(float, input().split()))

for i in range(len(a) - 1, -1, -1):
    if a[i] < 0:
        a.insert(i+1, 0.0)

print(a)