S = input()
A = float(input())
D = float(input())

with open(S, "w") as f:
    for i in range(10):
        f.write(str(A + i * D) + "\n")