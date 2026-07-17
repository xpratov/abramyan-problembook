def SwapRow(A, M, N, K1, K2):
    if K1 < 1 or K1 > M or K2 < 1 or K2 > M:
        return

    A[K1 - 1], A[K2 - 1] = A[K2 - 1], A[K1 - 1]


M = int(input("M = "))
N = int(input("N = "))

A = []
print("Matritsa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    A.append(row)

K1 = int(input("K1 = "))
K2 = int(input("K2 = "))

SwapRow(A, M, N, K1, K2)

print("Natija:")
for row in A:
    print(*row)