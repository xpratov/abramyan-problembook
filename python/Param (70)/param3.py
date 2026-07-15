def MinmaxNum(a, n):
    min_index = 0
    max_index = 0

    for i in range(1, n):
        if a[i] < a[min_index]:
            min_index = i
        if a[i] > a[max_index]:
            max_index = i

    return min_index + 1, max_index + 1

na = int(input())
A = list(map(float, input().split()))

nb = int(input())
B = list(map(float, input().split()))

nc = int(input())
C = list(map(float, input().split()))

print(*MinmaxNum(A, na))
print(*MinmaxNum(B, nb))
print(*MinmaxNum(C, nc))