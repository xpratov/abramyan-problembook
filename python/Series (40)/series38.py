k = int(input())

for i in range(k):
    old = int(input())

    increasing = True
    decreasing = True

    while True:
        x = int(input())

        if x == 0:
            break

        if x <= old:
            increasing = False

        if x >= old:
            decreasing = False

        old = x

    if increasing:
        print(1)
    elif decreasing:
        print(-1)
    else:
        print(0)