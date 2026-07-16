def SortArray(A, N):
    for i in range(N - 1):
        for j in range(i + 1, N):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]


NA = int(input())
A = list(map(float, input().split()))

NB = int(input())
B = list(map(float, input().split()))

NC = int(input())
C = list(map(float, input().split()))

SortArray(A, NA)
SortArray(B, NB)
SortArray(C, NC)

print(A)
print(B)
print(C)