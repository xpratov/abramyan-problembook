with open("SA", "r") as f:
    A = list(map(float, f.read().split()))

with open("SB", "r") as f:
    B = list(map(float, f.read().split()))

nA = int(len(A) ** 0.5)
nB = int(len(B) ** 0.5)

with open("SC", "w") as f:

    if nA != nB:
        pass

    else:
        n = nA

        for i in range(n):
            for j in range(n):

                s = 0

                for k in range(n):
                    s += A[i * n + k] * B[k * n + j]

                f.write(str(s) + " ")

            f.write("\n")