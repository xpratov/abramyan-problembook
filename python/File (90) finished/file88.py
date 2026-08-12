with open("input.txt", "r") as f:
    a = list(map(float, f.read().split()))

n = (len(a) + 2) // 3

index = 0

with open("output.txt", "w") as f:
    for i in range(n):
        for j in range(n):

            if abs(i - j) > 1:
                x = 0.0

            else:
                x = a[index]
                index += 1

            f.write(str(x) + " ")