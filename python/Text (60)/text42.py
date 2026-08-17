import math

A = float(input("A = "))
B = float(input("B = "))
N = int(input("N = "))

H = (B - A) / N

with open("result.txt", "w") as f:
    for i in range(N + 1):
        x = A + i * H
        y = math.sqrt(x)

        f.write(f"{x:>10.4f}{y:>15.8f}\n")