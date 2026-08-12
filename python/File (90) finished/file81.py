with open("input.txt", "r") as f:
    a = list(map(float, f.read().split()))

n = 0
while n * (n + 1) // 2 < len(a):
    n += 1

with open("output.txt", "w") as f:
    for x in a:
        f.write(str(x) + " ")