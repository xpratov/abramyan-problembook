k = int(input())

count = 0

for i in range(k):
    old = int(input())
    increasing = True

    while True:
        x = int(input())

        if x == 0:
            break

        if x <= old:
            increasing = False

        old = x

    if increasing:
        count += 1

print(count)