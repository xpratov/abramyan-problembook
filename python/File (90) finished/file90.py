with open("SA", "r") as f:
    A_data = list(map(float, f.read().split()))

with open("SB", "r") as f:
    B_data = list(map(float, f.read().split()))


nA = 0
while nA * (nA + 1) // 2 < len(A_data):
    nA += 1

nB = 0
while nB * (nB + 1) // 2 < len(B_data):
    nB += 1


with open("SC", "w") as f:

    if nA != nB:
        pass

    else:
        n = nA

        A = [[0.0] * n for _ in range(n)]
        B = [[0.0] * n for _ in range(n)]

        index = 0

        for i in range(n):
            for j in range(i + 1):
                A[i][j] = A_data[index]
                index += 1

        index = 0

        for i in range(n):
            for j in range(i + 1):
                B[i][j] = B_data[index]
                index += 1

        for i in range(n):
            for j in range(i + 1):

                s = 0.0

                for k in range(j, i + 1):
                    s += A[i][k] * B[k][j]

                f.write(str(s) + " ")