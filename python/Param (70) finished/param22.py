def SumCol(A, M, N, K):
    if K < 1 or K > N:
        return 0

    s = 0
    for i in range(M):
        s += A[i][K - 1]

    return s


M = int(input("Qatorlar soni (M): "))
N = int(input("Ustunlar soni (N): "))

A = []
print("Matritsa elementlarini kiriting:")
for i in range(M):
    row = list(map(float, input().split()))
    A.append(row)

K = int(input("K = "))

print(SumCol(A, M, N, K))