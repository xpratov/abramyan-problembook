def Split1(A, NA):
    B = []
    C = []

    for i in range(NA):
        if i % 2 == 0:
            B.append(A[i])
        else:
            C.append(A[i])

    NB = len(B)
    NC = len(C)

    return B, NB, C, NC

NA = int(input())
A = list(map(float, input().split()))

B, NB, C, NC = Split1(A, NA)

print(NB)
print(*B)

print(NC)
print(*C)