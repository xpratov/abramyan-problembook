with open("input.txt", "r") as f:
    a = list(map(float, f.read().split()))

n = int(len(a) ** 0.5)

with open("output.txt", "w") as f:
    for j in range(n):
        for i in range(n):
            index = i * n + j
            f.write(str(a[index]) + " ")
        f.write("\n")