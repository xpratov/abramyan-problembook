def Smooth1(a, n):
    b = a.copy()
    s = 0
    for i in range(n):
        s += b[i]
        a[i] = s / (i + 1)


n = int(input())
A = list(map(float, input().split()))

for _ in range(5):
    Smooth1(A, n)
    print(*A)