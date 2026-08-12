with open("input.txt", "r") as f:
    data = list(map(float, f.read().split()))

m = int(data[0])
a = data[1:]

n = len(a) // m

with open("output.txt", "w") as f:
    f.write(str(n) + "\n")

    for j in range(m):
        for i in range(n):
            index = i * m + j
            f.write(str(a[index]) + " ")
        f.write("\n")