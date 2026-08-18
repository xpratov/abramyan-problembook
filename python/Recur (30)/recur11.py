
def MaxElem(A, N):
    if N == 1:
        return A[0]

    max_old = MaxElem(A, N - 1)

    if A[N - 1] > max_old:
        return A[N - 1]
    return max_old


A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

print(MaxElem(A, len(A)))
print(MaxElem(B, len(B)))
print(MaxElem(C, len(C)))