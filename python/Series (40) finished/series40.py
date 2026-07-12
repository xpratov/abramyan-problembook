k = int(input())

for i in range(k):
    a = []

    while True:
        x = int(input())
        if x == 0:
            break
        a.append(x)

    pos = 0

    for j in range(1, len(a)-1):
        if not ((a[j] > a[j-1] and a[j] > a[j+1]) or
                (a[j] < a[j-1] and a[j] < a[j+1])):
            pos = j + 1
            break

    if pos == 0:
        print(len(a))
    else:
        print(pos)