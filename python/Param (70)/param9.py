def RemoveForInc(a, n):
    i = 1
    while i < n:
        if a[i] < a[i - 1]:
            a.pop(i)
            n -= 1
        else:
            i += 1
    return n


na = int(input())
A = list(map(float, input().split()))

nb = int(input())
B = list(map(float, input().split()))

nc = int(input())
C = list(map(float, input().split()))

na = RemoveForInc(A, na)
nb = RemoveForInc(B, nb)
nc = RemoveForInc(C, nc)

print(na)
print(*A)
print(nb)
print(*B)
print(nc)
print(*C)