k = int(input())

total = 0

for i in range(k):
    length = 0

    while True:
        x = int(input())

        if x == 0:
            break

        length += 1

    print(length)
    total += length

print(total)