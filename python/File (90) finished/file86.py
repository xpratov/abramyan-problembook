with open("input.txt", "r") as f:
    a = list(map(float, f.read().split()))

n = 0
while n * (n + 1) // 2 < len(a):
    n += 1

index = 0

with open("output.txt", "w") as f:
    for i in range(n):
        for j in range(n):
            if j < i:
                x = 0.0
            else:
                x = a[index]
                index += 1

            f.write(str(x) + " ")