def Smooth2(a, n):
    b = a.copy()
    for i in range(1, n):
        a[i] = (b[i - 1] + b[i]) / 2


n = int(input())
A = list(map(float, input().split()))

for _ in range(5):
    Smooth2(A, n)
    print(*A)