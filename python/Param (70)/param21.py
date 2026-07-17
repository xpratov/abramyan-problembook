def SumRow(A, M, N, K):
    if K < 1 or K > M:
        return 0

    s = 0
    for j in range(N):
        s += A[K - 1][j]

    return s


M = int(input("Qatorlar soni (M): "))
N = int(input("Ustunlar soni (N): "))

A = []
print("Matritsa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    A.append(row)

K = int(input("K = "))

print(SumRow(A, M, N, K))