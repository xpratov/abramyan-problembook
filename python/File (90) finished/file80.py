with open("input.txt", "r") as f:
    a = list(map(float, f.read().split()))

count = len(a)

n = 0

while n * (n + 1) // 2 < count:
    n += 1

with open("output.txt", "w") as f:

    index = 0

    for i in range(n):
        for j in range(i, n):
            f.write(str(a[index]) + " ")
            index += 1

        f.write("\n")