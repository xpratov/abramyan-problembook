with open("input.txt", "r") as f:
    a = list(map(float, f.read().split()))

with open("output.txt", "w") as f:
    for x in a:
        f.write(str(x) + " ")