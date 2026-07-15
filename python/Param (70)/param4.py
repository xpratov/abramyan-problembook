def Inv(a, n):
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]


na = int(input())
A = list(map(float, input().split()))

nb = int(input())
B = list(map(float, input().split()))

nc = int(input())
C = list(map(float, input().split()))

Inv(A, na)
Inv(B, nb)
Inv(C, nc)

print(*A)
print(*B)
print(*C)