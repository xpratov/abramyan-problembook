def MaxNum(a, n):
    max_index = 0
    for i in range(1, n):
        if a[i] > a[max_index]:
            max_index = i
    return max_index + 1   # tartib raqami (1 dan boshlanadi)


na = int(input())
A = list(map(float, input().split()))

nb = int(input())
B = list(map(float, input().split()))

nc = int(input())
C = list(map(float, input().split()))

print(MaxNum(A, na))
print(MaxNum(B, nb))
print(MaxNum(C, nc))