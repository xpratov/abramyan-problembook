def Hill(A, N):
    A.sort()

    B = [0] * N

    left = 0
    right = N - 1

    for i in range(N):
        if i % 2 == 0:
            B[left] = A[i]
            left += 1
        else:
            B[right] = A[i]
            right -= 1

    for i in range(N):
        A[i] = B[i]

NA = int(input())
A = list(map(float, input().split()))

NB = int(input())
B = list(map(float, input().split()))

NC = int(input())
C = list(map(float, input().split()))

Hill(A, NA)
Hill(B, NB)
Hill(C, NC)

print(A)
print(B)
print(C)