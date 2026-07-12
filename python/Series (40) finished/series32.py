k = int(input())
n = int(input())

for i in range(k):
    a = list(map(int, input().split()))

    if 2 in a:
        print(a.index(2) + 1)
    else:
        print(0)