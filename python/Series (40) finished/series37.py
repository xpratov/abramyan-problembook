k = int(input())

count = 0

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

    if increasing or decreasing:
        count += 1

print(count)