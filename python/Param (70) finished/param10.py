def DoubleX(a, n, x):
    i = 0
    while i < n:
        if a[i] == x:
            a.insert(i + 1, x)
            n += 1
            i += 2
        else:
            i += 1
    return n


na = int(input())
A = list(map(int, input().split()))
xa = int(input())

nb = int(input())
B = list(map(int, input().split()))
xb = int(input())

nc = int(input())
C = list(map(int, input().split()))
xc = int(input())

na = DoubleX(A, na, xa)
nb = DoubleX(B, nb, xb)
nc = DoubleX(C, nc, xc)

print(na)
print(*A)
print(nb)
print(*B)
print(nc)
print(*C)