import math

A = float(input("A = "))
B = float(input("B = "))
N = int(input("N = "))

H = (B - A) / N

with open("result.txt", "w") as f:
    for i in range(N + 1):
        x = A + i * H

        sin_x = math.sin(x)
        cos_x = math.cos(x)

        f.write(f"{x:>8.4f}{sin_x:>12.8f}{cos_x:>12.8f}\n")