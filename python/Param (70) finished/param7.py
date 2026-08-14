def Smooth3(a, n):
    b = a.copy()
    if n > 1:
        a[0] = (b[0] + b[1]) / 2
        a[n - 1] = (b[n - 2] + b[n - 1]) / 2
    for i in range(1, n - 1):
        a[i] = (b[i - 1] + b[i] + b[i + 1]) / 3


n = int(input())
A = list(map(float, input().split()))

for _ in range(5):
    Smooth3(A, n)
    print(*A)