I = int(input())
J = int(input())

with open("input.txt", "r") as f:
    a = list(map(float, f.read().split()))

n = 0

while n * (n + 1) // 2 < len(a):
    n += 1

print(n)

if I > n or J > n:
    print(-1.0)

elif J < I:
    print(0.0)

else:
    index = (I - 1) * n - (I - 1) * (I - 2) // 2 + (J - I)
    print(a[index])