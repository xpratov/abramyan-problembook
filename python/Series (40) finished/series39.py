k = int(input())

count = 0

for i in range(k):
    a = []

    while True:
        x = int(input())
        if x == 0:
            break
        a.append(x)

    saw = True

    for j in range(1, len(a)-1):
        if not ((a[j] > a[j-1] and a[j] > a[j+1]) or
                (a[j] < a[j-1] and a[j] < a[j+1])):
            saw = False
            break

    if saw:
        count += 1

print(count)