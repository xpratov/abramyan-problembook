k = int(input())
n = int(input())

for i in range(k):
    a = list(map(int, input().split()))

    pos = 0
    for j in range(n):
        if a[j] == 2:
            pos = j + 1

    print(pos)